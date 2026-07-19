import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from application.app import app


def test_home_endpoint():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    response_data = response.get_json()

    assert response_data["status"] == "running"
    assert response_data["application"] == "AI Cloud Reliability platform Demo"


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    response_data = response.get_json()

    assert response_data["status"] == "healthy"
    assert response_data["service"] == "reliability-demo"


def test_simulated_error_endpoint():
    client = app.test_client()

    response = client.get("/simulate-error")

    assert response.status_code == 500

    response_data = response.get_json()

    assert response_data["status"] == "error"


def test_metrics_endpoint():
    client = app.test_client()

    client.get("/")
    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"application_http_requests_total" in response.data