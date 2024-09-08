#!/usr/bin/env python
# coding: utf-8

from haystack.document_stores.in_memory import InMemoryDocumentStore

document_store = InMemoryDocumentStore()


from haystack import Document 


from pathlib import Path


get_ipython().system('ls ../')


doc_content = Path("../rick_and_morty_episodes.txt").read_text()


docs = [Document(content=doc_content)]


docs


from haystack.components.embedders import SentenceTransformersDocumentEmbedder

doc_embedder = SentenceTransformersDocumentEmbedder(model="sentence-transformers/all-MiniLM-L6-v2")
doc_embedder.warm_up()


ls ~/.cache/huggingface/hub | grep sentence-transformers


docs_with_embeddings = doc_embedder.run(docs)
document_store.write_documents(docs_with_embeddings["documents"])


# ⚠️ Notice that you used sentence-transformers/all-MiniLM-L6-v2 model to create embeddings for your documents before. This is why you need to use the same model to embed the user queries.

from haystack.components.embedders import SentenceTransformersTextEmbedder

text_embedder = SentenceTransformersTextEmbedder(model="sentence-transformers/all-MiniLM-L6-v2")


from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever

retriever = InMemoryEmbeddingRetriever(document_store)


from haystack.components.builders import PromptBuilder

template = """
Given the following information, answer the question.

Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{question}}
Answer:
"""

prompt_builder = PromptBuilder(template=template)


import os
from getpass import getpass
from haystack.components.generators import OpenAIGenerator

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass("Enter OpenAI API key:")

generator = OpenAIGenerator(model="gpt-4o-mini")


from haystack import Pipeline

basic_rag_pipeline = Pipeline()
# Add components to your pipeline
basic_rag_pipeline.add_component("text_embedder", text_embedder)
basic_rag_pipeline.add_component("retriever", retriever)
basic_rag_pipeline.add_component("prompt_builder", prompt_builder)
basic_rag_pipeline.add_component("llm", generator)

# Now, connect the components to each other
basic_rag_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
basic_rag_pipeline.connect("retriever", "prompt_builder.documents")
basic_rag_pipeline.connect("prompt_builder", "llm")


question = "What is a Meeseeks Box?"

response = basic_rag_pipeline.run({"text_embedder": {"text": question}, "prompt_builder": {"question": question}})

print(response["llm"]["replies"][0])


question = """
Give me a list of all the episodes about Jessica, in JSON format

e.g.

[
    {
        "season_number": 1,
        "episode_number": 3,
        "episode_name": "...",
        "episode_description": "..."
    },
    ...
]
""".strip()

response = basic_rag_pipeline.run({"text_embedder": {"text": question}, "prompt_builder": {"question": question}})

print(response["llm"]["replies"][0])


response







