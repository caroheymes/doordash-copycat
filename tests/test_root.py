# tests/test_root.py

def test_root_endpoint(client):
    """
    Test that the root endpoint '/' returns the welcome message with status 200.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the DoorDash Delivery Fee Service API"}