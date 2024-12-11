from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/value', methods=['GET'])
def get_value():
    # In a real scenario, this might be something dynamic,
    # for now let's return a static value or maybe a random number
    import random
    value = random.randint(1, 100)
    return jsonify({"value": value})

if __name__ == '__main__':
    # Note: In production, you'd use a WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=5000)
