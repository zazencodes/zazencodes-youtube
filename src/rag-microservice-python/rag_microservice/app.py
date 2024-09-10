from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack import Document
from haystack.components.embedders import (
    SentenceTransformersDocumentEmbedder,
    SentenceTransformersTextEmbedder,
)
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
from haystack.components.builders import PromptBuilder
from haystack.components.generators import OpenAIGenerator
from haystack import Pipeline
from pathlib import Path
import os

CORPUS_DOCUMENTS_PATH = os.environ["CORPUS_DOCUMENTS_PATH"]
CORPUS_DOCUMENTS_FILE_EXT = os.environ["CORPUS_DOCUMENTS_FILE_EXT"]
TEXT_EMBEDDING_MODEL = os.environ["TEXT_EMBEDDING_MODEL"]
OPENAI_GENERATOR_MODEL = os.environ["OPENAI_GENERATOR_MODEL"]

if "OPENAI_API_KEY" not in os.environ:
    raise ValueError(f"OPENAI_API_KEY environment variable is not set")

# FastAPI app initialization
app = FastAPI()


# Request body for the API
class QuestionRequest(BaseModel):
    question: str


# Step 1: Create the document store
def create_document_store() -> InMemoryDocumentStore:
    print("Instantiating RAG document store")
    document_store = InMemoryDocumentStore()
    return document_store


# Step 2: Read documents and embed them
def embed_documents(document_store: InMemoryDocumentStore) -> None:
    doc_files = Path(CORPUS_DOCUMENTS_PATH).glob(f"**/*.{CORPUS_DOCUMENTS_FILE_EXT}")
    print(f"Loaded documents for RAG: {doc_files}")

    doc_contents = [f.read_text() for f in doc_files]
    docs = [Document(content=content) for content in doc_contents]

    doc_embedder = create_document_embedder()
    doc_embedder.warm_up()
    docs_with_embeddings = doc_embedder.run(docs)
    document_store.write_documents(docs_with_embeddings["documents"])


def create_document_embedder() -> SentenceTransformersDocumentEmbedder:
    print(f"Embedding documents with {TEXT_EMBEDDING_MODEL}")
    document_embedder = SentenceTransformersDocumentEmbedder(
        model=TEXT_EMBEDDING_MODEL,
    )
    return document_embedder


def create_text_embedder() -> SentenceTransformersTextEmbedder:
    print(f"Embedding text with {TEXT_EMBEDDING_MODEL}")
    text_embedder = SentenceTransformersTextEmbedder(
        model=TEXT_EMBEDDING_MODEL,
    )
    return text_embedder


# Step 4: Create the retriever
def create_retriever(
    document_store: InMemoryDocumentStore,
) -> InMemoryEmbeddingRetriever:
    retriever = InMemoryEmbeddingRetriever(document_store=document_store)
    return retriever


# Step 5: Create the prompt builder
def create_prompt_builder() -> PromptBuilder:
    template = """
    Given the following information, answer the question.

    Context:
    {% for document in documents %}
        {{ document.content }}
    {% endfor %}

    Question: {{question}}
    Answer:
    """
    print(f"Instantiating prompt template:\n{template}")
    prompt_builder = PromptBuilder(template=template)
    return prompt_builder


# Step 6: Create the generator (OpenAI-based)
def create_generator() -> OpenAIGenerator:
    print(f"Instantiating OpenAI generator with model {OPENAI_GENERATOR_MODEL}")
    generator = OpenAIGenerator(model=OPENAI_GENERATOR_MODEL)
    return generator


# Step 7: Build the RAG pipeline
def create_rag_pipeline(
    text_embedder: SentenceTransformersTextEmbedder,
    retriever: InMemoryEmbeddingRetriever,
    prompt_builder: PromptBuilder,
    generator: OpenAIGenerator,
) -> Pipeline:
    print("Building RAG pipeline")

    rag_pipeline = Pipeline()
    rag_pipeline.add_component("text_embedder", text_embedder)
    rag_pipeline.add_component("retriever", retriever)
    rag_pipeline.add_component("prompt_builder", prompt_builder)
    rag_pipeline.add_component("llm", generator)

    # Connect components in the pipeline
    rag_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
    rag_pipeline.connect("retriever", "prompt_builder.documents")
    rag_pipeline.connect("prompt_builder", "llm")

    print(f"Done building RAG pipeline: {rag_pipeline}")

    return rag_pipeline


# Load the pipeline on startup and store it in `app.state`
@app.on_event("startup")
async def load_pipeline():
    document_store = create_document_store()
    embed_documents(document_store)

    text_embedder = create_text_embedder()
    retriever = create_retriever(document_store)
    prompt_builder = create_prompt_builder()
    generator = create_generator()

    rag_pipeline = create_rag_pipeline(
        text_embedder=text_embedder,
        retriever=retriever,
        prompt_builder=prompt_builder,
        generator=generator,
    )

    # Store the pipeline in the app's state
    app.state.rag_pipeline = rag_pipeline


# Define the endpoint for answering questions
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        # Access the pipeline from the app's state
        rag_pipeline: Pipeline = app.state.rag_pipeline
        question = request.question
        response = rag_pipeline.run(
            {
                "text_embedder": {"text": question},
                "prompt_builder": {"question": question},
            }
        )
        return {"answer": response["llm"]["replies"][0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
