# 4-env-variables

Run app:

```bash
docker build -t iris-logistic-demo .
docker run --rm \
    -e RANDOM_SEED=137 -e C_REG_STRENGTH=0.1 \
    iris-logistic-demo
docker run --rm --env-file=.env iris-logistic-demo
```

