FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Ensure python outputs are displayed during runtime
ENV PYTHONUNBUFFERED=1

ENV CORPUS_DOCUMENTS_PATH=/data
ENV CORPUS_DOCUMENTS_FILE_EXT="txt"
ENV TEXT_EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
ENV OPENAI_GENERATOR_MODEL="gpt-4o-mini"

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

