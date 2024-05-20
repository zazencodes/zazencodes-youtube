# Kubernetes

## Docs
- https://minikube.sigs.k8s.io/docs/start/

## Demo

- [ ] Containerize the FastAPI Application
- [ ] Build and test the Docker Image

```bash
docker build -t fastapi-app .
docker run --rm -p 80:80 fastapi-app
curl http://0.0.0.0/version
```

- [ ] Stop container and clean up docker images

- [ ] Set Up a Local Kubernetes Cluster (Minikube)

```bash
# Install on MacOS
# For other operating systems, see official docs: https://minikube.sigs.k8s.io/docs/start/
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-arm64
sudo install minikube-darwin-arm64 /usr/local/bin/minikube
```

- [ ] Start cluster

```bash
# Start cluster
minikube start
```

- [ ] Open dashboard

```bash
minikube dashboard
```

- [ ] Apply Kubernetes Manifests to local cluster

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

- [ ] Build and Load Docker Image into Minikube

```bash
eval $(minikube docker-env) # this step configures your shell environment so that the Docker CLI communicates
                            # with the Docker daemon inside the Minikube VM instead of the one on your host machine
docker build -t fastapi-app .
```

- [ ] Show services launch our app

```bash
kubectl get services
kubectl get pods
minikube service fastapi-service
```

- [ ] Test the app and view the logs

```bash
SERVICE_1= # set service pod name
SERVICE_2= # set service pod name
SERVICE_3= # set service pod name
APP_URI="http://127.0.0.1:63574" # e.g.
kubectl logs $SERVICE_1
kubectl logs $SERVICE_2
kubectl logs $SERVICE_3
curl $APP_URI/version
kubectl logs $SERVICE_1
kubectl logs $SERVICE_2
kubectl logs $SERVICE_3
curl -X POST -d '{"x": 3.3, "y": 2.5}' -H "Content-Type: application/json" $APP_URI/add
kubectl logs $SERVICE_1
kubectl logs $SERVICE_2
kubectl logs $SERVICE_3
```

- [ ] Teardown

```bash
minikube stop
minikube delete --all --purge
```


