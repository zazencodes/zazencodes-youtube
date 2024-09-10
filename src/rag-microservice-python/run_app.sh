#!/bin/bash
docker build . -t zazencodes/rag-microservice:latest
docker run -d --rm \
    -p 8000:8000 \
    --env-file .env \
    -v ./data:/data \
    -v ./rag_microservice:/app \
    zazencodes/rag-microservice:latest
