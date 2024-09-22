#!/bin/bash
#
# Run on server
#
#
docker pull registry.digitalocean.com/zazencodes/rag-microservice:linux
docker run --rm \
    -p 8000:8000 \
    --env-file .env \
    -v ./data:/data \
    registry.digitalocean.com/zazencodes/rag-microservice:linux
