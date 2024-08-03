# 5-compose

Run app:

```bash
docker compose up --build
```


Make prediction:
```bash
curl localhost:5000/predict -X POST -d '{"x1": 12, "x2": 94}'
```
