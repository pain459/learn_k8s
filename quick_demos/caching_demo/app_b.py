from flask import Flask, jsonify
import os
import requests
import redis

app = Flask(__name__)

# Configure Redis client
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', '6379'))
cache_ttl = int(os.environ.get('CACHE_TTL', '300'))  # default 5 min = 300 sec
r = redis.Redis(host=redis_host, port=redis_port, db=0)

# Configure App A endpoint
app_a_host = os.environ.get('APP_A_HOST', 'app-a')
app_a_port = os.environ.get('APP_A_PORT', '5000')
app_a_url = f"http://{app_a_host}:{app_a_port}/value"

@app.route('/cached-value', methods=['GET'])
def get_cached_value():
    cached = r.get('the_value')
    if cached:
        # If found in Redis, return it
        return jsonify({"source": "redis", "value": int(cached)})
    else:
        # If not found, fetch from App A
        resp = requests.get(app_a_url)
        if resp.status_code == 200:
            value = resp.json().get('value')
            # Store in Redis with TTL
            r.setex('the_value', cache_ttl, value)
            return jsonify({"source": "appA", "value": value})
        else:
            return jsonify({"error": "Failed to retrieve value from App A"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
