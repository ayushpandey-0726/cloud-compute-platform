def test_create_instance(client):
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


def test_get_instance(client):
    create_response = client.post(
        "/instances",
        json={
            "name": "web-server",
            "cpu": 4,
            "memory": 8,
            "region": "us-east",
        },
    )

    instance_id = create_response.json()["id"]

    response = client.get(f"/instances/{instance_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == instance_id
    assert data["name"] == "web-server"


def test_get_nonexistent_instance(client):
    response = client.get("/instances/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Instance not found"
