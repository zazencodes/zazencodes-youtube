# 1-spin-up-db

Spin up Redis container:
```bash
docker run --rm --name my-redis -p 6379:6379 redis

```
Spin up Postgres container:
```bash
docker run --rm --name my-postgres -p 5432:5432 \
    -e POSTGRES_PASSWORD=mysecretpassword postgres
```
