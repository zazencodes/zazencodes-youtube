# RAG Microservice with Docker and Python

1. Create a `.env` file and add an `OPENAI_API_KEY` environment variable
2. Run app

```bash
./run_app.sh
```

3. Test and make RAG requests

```bash
curl "http://localhost:8000/health"
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d '{"question": "What is a Meeseeks Box?"}'
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d '{"question": "Give me a list of all the episodes about Jessica, including episode descriptions, in JSON format."}'
```


