import pytest
import httpx

@pytest.fixture(scope="module")
def client():
    """
    HTTP client that makes real network calls to the DoorDash API 
    running inside the Docker container on port 8080.
    """
    base_url = "http://localhost:8080"
    with httpx.Client(base_url=base_url) as client:
        yield client