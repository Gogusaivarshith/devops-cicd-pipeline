import os
import time

from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "HTTP request latency",
    ["endpoint"],
)


@app.before_request
def start_timer():
    from flask import g
    g.request_start = time.perf_counter()


@app.after_request
def record_request(response):
    from flask import request, g
    start = getattr(g, "request_start", time.perf_counter())
    elapsed = time.perf_counter() - start

    REQUEST_COUNT.labels(
        request.method,
        request.path,
        response.status_code,
    ).inc()

    REQUEST_LATENCY.labels(request.path).observe(elapsed)
    return response


@app.get("/")
def index():
    return jsonify({
        "application": "devops-demo",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "status": "running",
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.get("/ready")
def ready():
    return jsonify({"status": "ready"}), 200


app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    "/metrics": make_wsgi_app()
})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
