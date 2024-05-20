# Airflow

- [ ] Fetch docker compose from apache.org

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml'
```

- [ ] Look at `zc_demo.py` in dags folder


- [ ] Initialize the database

```bash
docker compose up airflow-init
```

- [ ] Start the airflow server

```bash
docker compose up
```

- [ ] Load server at http://0.0.0.0:8080/ and login with username and password "airflow"

- [ ] Run zc_demo DAG


