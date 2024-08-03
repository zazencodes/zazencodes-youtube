# 3-app-volume

Run app:

```bash
docker build -t simple-ml-app .
docker run \
    --rm --name simple-ml-app-1 \
    -v ./app:/app -v ./data:/data -v ./artifacts:/artifacts \
    simple-ml-app
```


