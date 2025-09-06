from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_client_returns_success():
    response = client.post(
        "/api/contacts/", json={"name": "John Doe", "email": "john.doe@example.com"}
    )

    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
