import redis

# Connect to Redis
r = redis.Redis(host='redis', port=6379)

# Set a key
r.set('message', 'Hello from Python!')

# Get the key
msg = r.get('message')
print(f'Redis says: {msg.decode()}')
