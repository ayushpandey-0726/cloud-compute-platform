from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_instance():
    payload = {
        "name": "web-server",
        "cpu": 4,
        "memory": 8,
        "region": "us-east",
    }

    response = client.post("/instances", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "web-server"
    assert data["cpu"] == 4
    assert data["memory"] == 8
    assert data["region"] == "us-east"
    assert data["status"] == "RUNNING"
