# Kubernetes

- [ ] Containerize the FastAPI Application
- [ ] Build the Docker Image

```bash
docker build -t fastapi-app .
```

- [ ] Set Up a Local Kubernetes Cluster (Minikube)

```bash
# Install on MacOS
# For other operating systems, see official docs: https://minikube.sigs.k8s.io/docs/start/
curl -LO https://github.com/kubernetes/minikube/releases/download/v1.33.1/minikube-darwin-arm64
sudo install minikube-darwin-amd64 /usr/local/bin/minikube

```
```bash
# Start cluster
minikube start
```

- [ ] Apply Kubernetes Manifests to local cluster

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

- [ ] Build and Load Docker Image into Minikube

```bash
eval $(minikube docker-env)
minikube ip
```
- [ ] Test deployment: `http://<Minikube_IP>:30001/version`





