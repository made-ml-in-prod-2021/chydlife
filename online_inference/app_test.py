from fastapi.testclient import TestClient
from app import app


client = TestClient(app)

def test_main():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200