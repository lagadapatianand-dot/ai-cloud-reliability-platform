from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest
from werkzeug.wrappers import Response

app = Flask(__name__)

REQUEST_COUNTER = Counter(
    "application_http_requests_total",
    "Total number of HTTP requests",
    ["endpoint", "status"],
)


@app.get("/")
def home():
    REQUEST_COUNTER.labels(endpoint="/", status="200").inc()

    return jsonify(
        application="AI Cloud Reliability platform Demo",
        status="running",
        message="The application is running successfully.",
    )


@app.get("/health")
def health():
    REQUEST_COUNTER.labels(endpoint="/health", status="200").inc()

    return jsonify(
        service="reliability-demo",
        status="healthy",
    )


@app.get("/simulate-error")
def simulate_error():
    REQUEST_COUNTER.labels(endpoint="/simulate-error", status="500").inc()

    return jsonify(
        status="error",
        message="This is a controlled test failure.",
    ), 500


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        content_type="text/plain; version=0.0.4",
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )