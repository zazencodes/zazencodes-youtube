
# Japanese Translator API

A FastAPI-based service that translates English text to Japanese using OpenAI's GPT-4 model.

## Features

- Translate English text to Japanese
- RESTful API endpoint
- Powered by OpenAI's GPT-4
- Built with FastAPI

## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install fastapi uvicorn openai
```
3. Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

1. Start the server:
```bash
python main.py
```

2. The API will be available at `http://localhost:8080`

3. Use the `/translate` endpoint with a POST request:
```bash
curl -X POST "http://localhost:8080/translate" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, how are you?"}'
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`



## Deployment to Google Cloud Compute Engine

1. Install Google Cloud SDK and initialize:
```bash
# Install Google Cloud SDK (follow instructions for your OS)
gcloud init
```

2. Create a new VM instance:
```bash
gcloud compute instances create japanese-translator \
    --zone=us-central1-a \
    --machine-type=e2-micro \
    --image-family=debian-11 \
    --image-project=debian-cloud \
    --tags=http-server

```
3. Create a firewall rule to allow HTTP traffic:
```bash
gcloud compute firewall-rules create allow-http \
    --target-tags http-server \
    --allow tcp:8080
```

4. Get the external IP:
```bash
gcloud compute instances describe japanese-translator \
    --zone=us-central1-a \
    --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
```

5. Copy files to the instance:
```bash
gcloud compute scp *.* japanese-translator:~/
```


6. SSH into the instance:
```bash
gcloud compute ssh japanese-translator --zone=us-central1-a
```

7. Install dependencies

```bash
apt-get update
apt-get install -y python3-pip
pip3 install -r requirements.txt
export OPENAI_API_KEY="your-api-key-here"
```


Your API will be available at `http://YOUR_EXTERNAL_IP:8080`

