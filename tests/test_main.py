from fastapi.testclient import TestClient
from app.main import app, hello_world

client = TestClient(app)


def test_create_client_returns_success():
    pass


def test_hello_world():
    assert hello_world() == "Hello World!"
