import os
import pytest
import httpx

@pytest.fixture(scope="module")
def client():
    """
    HTTP client that makes real network calls to the DoorDash API.
    Uses the API_PORT environment variable if set, defaulting to 8080.
    """
    port = os.getenv("API_PORT", "8080")
    base_url = f"http://localhost:{port}"
    with httpx.Client(base_url=base_url) as client:
        yield client