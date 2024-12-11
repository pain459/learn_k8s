from flask import Flask, jsonify
import os
import requests
import redis

app = Flask(__name__)

# Configuration
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', '6379'))
cache_ttl = int(os.environ.get('CACHE_TTL', '300'))  # default 5 min = 300 sec

# Redis client
r = redis.Redis(host=redis_host, port=redis_port, db=0)

# App A endpoint configuration
app_a_host = os.environ.get('APP_A_HOST', 'app-a')
app_a_port = os.environ.get('APP_A_PORT', '5000')
app_a_url = f"http://{app_a_host}:{app_a_port}/value"

@app.route('/cached-value', methods=['GET'])
def get_cached_value():
    # Try to get the value from Redis
    cached_value = r.get('the_value')
    if cached_value is not None:
        # Value found in cache, return it
        return jsonify({"source": "redis", "value": int(cached_value)})

    # Value not found in cache, fetch from App A
    response = requests.get(app_a_url)
    if response.status_code == 200:
        value = response.json().get('value')
        # Store the value in Redis with a 5-minute TTL
        r.setex('the_value', cache_ttl, value)
        return jsonify({"source": "appA", "value": value})
    else:
        # Could not retrieve from App A
        return jsonify({"error": "Failed to retrieve value from App A"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
