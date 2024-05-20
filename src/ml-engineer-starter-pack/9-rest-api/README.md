# REST API

## Using REST APIs

DigitalOcean services status
```python
import requests

url = "https://status.digitalocean.com/api/v2/status.json"
resp = requests.get(url)
resp
resp.json()

```

## Creating a RESP API


```bash
fastapi dev demo.py
curl http://localhost:8000/version
curl -X POST -d '{"x": 3.3, "y": 2.5}' -H "Content-Type: application/json" http://localhost:8000/add

```


