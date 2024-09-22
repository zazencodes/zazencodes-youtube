# RAG Microservice with Docker and Python

## Local deployment

1. Create a `.env` file and add an `OPENAI_API_KEY` environment variable.

2. Run app:
```bash
./run_app.sh
```

3. Test and make RAG requests from local machine:
```bash
SERVER_IP = # Set server IP address, or localhost
curl "http://$SERVER_IP:8000/health"
curl -X POST "http://$SERVER_IP:8000/ask" -H "Content-Type: application/json" -d '{"question": "What is a Meeseeks Box?"}'
curl -X POST "http://$SERVER_IP:8000/ask" -H "Content-Type: application/json" -d '{"question": "Give me a list of all the episodes about Jessica, including episode descriptions, in JSON format."}'
```

## Basic server deployment

1. Create a `.env` file and add an `OPENAI_API_KEY` environment variable.

2. Copy source code to server:
```bash
SERVER_IP = # Set server IP address, or localhost
./deploy_app.sh
scp -r deploy root@$SERVER_IP:/root/rag-microservice
```

3. Follow steps above for Local deployment to run app on server.

## Container registry deployment

1. Build and upload to digital ocean container registry:

```bash
# Build for linux/amd64 system, from mac
docker buildx create --use
docker buildx build --platform linux/amd64 -t registry.digitalocean.com/zazencodes/rag-microservice:linux --push . -f Dockerfile.deploy
```

2. Create a `.env` file and add an `OPENAI_API_KEY` environment variable on
   server.

3. Run on server:
```bash
./run_deployment.sh
```

## Kubernetes deployment

1. Create a `.env` file and add an `OPENAI_API_KEY` environment variable.

2. Build and upload docker image to container registry:
```bash
# Build for linux/amd64 system, from mac
docker buildx create --use
docker buildx build --platform linux/amd64 -t registry.digitalocean.com/zazencodes/rag-microservice:k8s --push . -f Dockerfile.k8s_deploy
```

3. Link container registry with kubernetes cluster in digital ocean. Go to
   settings of container registry and give k8s pod cluster permission to pull
images.

4. Deploy to kubernetes
```bash
# Bundle .env into secrets
kubectl create secret generic rag-microservice-secret --from-env-file=.env

# Add to cluster
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Restart cluster, if needed
kubectl rollout restart deployment rag-microservice-deployment
```

5. Make requests to load balancer external IP and monitor pods:
```bash
SERVER_IP = # Set to external IP for load balancer
curl "http://$SERVER_IP/health"
curl -X POST "http://$SERVER_IP/ask" -H "Content-Type: application/json" -d '{"question": "Tell me about my fave character, Mr. Nibmus!"}'

# Monitor pods
kubectl get pods
kubectl describe pods [POD_ID]
kubectl logs [POD_ID]
```
