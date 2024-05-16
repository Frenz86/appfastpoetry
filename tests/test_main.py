import pytest
from starlette.testclient import TestClient

from backend.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_base_route(client):
    """
    GIVEN a FASTAPI application
    WHEN the '/' route is requested (GET)
    THEN check the response is valid
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
