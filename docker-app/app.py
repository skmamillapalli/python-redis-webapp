from flask import Flask
import redis, os

app=Flask(__name__)
redis_host=os.environ.get("REDIS_HOST", 'redis')
redis_obj = redis.Redis(host=redis_host, port=6379)
from flask import logging

@app.route("/hello")
def hello():
    # Keep the access count
    app.logger.info('accessing redis')
    redis_obj.incr('hits')
    access_count = redis_obj.get('hits')
    return f"Hello World! I've been accessed {access_count} times"

@app.route("/ping")
def ping():
    return "Available!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)