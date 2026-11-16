import os
import socket

from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUESTS = Counter("app_requests_total", "Total HTTP requests", ["endpoint"])


@app.get("/")
def index():
    REQUESTS.labels(endpoint="/").inc()
    return jsonify(
        message="Hello from the demo service",
        host=socket.gethostname(),
        version=os.getenv("APP_VERSION", "dev"),
    )


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
