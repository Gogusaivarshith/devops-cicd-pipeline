import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from app.app import app


def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["application"] == "devops-demo"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_ready():
    client = app.test_client()
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json["status"] == "ready"


def test_metrics():
    client = app.test_client()
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"http_requests_total" in response.data
