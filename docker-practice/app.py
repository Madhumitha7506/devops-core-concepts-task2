import os

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, socket_connect_timeout=2)


@app.route("/")
def hello():
    try:
        count = cache.incr("hits")
        return f"Hello from Docker Compose! This page has been viewed {count} times.\n"
    except redis.exceptions.RedisError:
        return "Hello from Docker! Redis is not connected.\n"


@app.route("/health")
def health():
    return "ok\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
