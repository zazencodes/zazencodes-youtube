# Example - Configuring Redis using a ConfigMap

https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap/

Configure a Redis cache using data stored in a ConfigMap:

```bash
# Generate config file redis-pod.yaml
python generate_yaml_config.py


# Create a ConfigMap with an empty configuration block:

cat <<EOF >./example-redis-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-redis-config
data:
  redis-config: ""
EOF


# Apply the ConfigMap created above
kubectl apply -f example-redis-config.yaml


# Apply the Redis pod manifest
kubectl apply -f redis-pod.yaml
```

