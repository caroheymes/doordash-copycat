# tests/test_health.py

def test_health_endpoint(client):
    """
    Test that the health endpoint '/status/' returns the service status with status 200.
    """
    response = client.get("/status/")
    assert response.status_code == 200
    assert response.json() == {"status": "Service is up and running"}
