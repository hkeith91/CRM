from fastapi.testclient import TestClient
from starlette.types import Message
from app.main import app, hello_world

client = TestClient(app)

"""
def test_create_client_returns_success():
    response = client.post(
        "/api/contacts/", json={"name": "John Doe", "email": "john.doe@example.com"}
    )

    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
"""


def test_hello_world():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
