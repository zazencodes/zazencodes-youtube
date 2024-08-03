import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Write data to Redis
r.set('foo', 'bar')

# Read data from Redis
value = r.get('foo')
print(f"Value from Redis: {value.decode('utf-8')}")
