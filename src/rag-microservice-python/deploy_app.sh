#!/bin/bash

rm -r deploy
mkdir deploy

cp -r rag_microservice deploy
cp -r data deploy

cp run_app.sh deploy
cp Dockerfile deploy
cp requirements.txt deploy
cp .env deploy
