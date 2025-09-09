from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_client_returns_success():
    response = client.post(
        "/api/contacts/",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"


def test_hello_world():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
