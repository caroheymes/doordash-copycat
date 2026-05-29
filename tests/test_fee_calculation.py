# tests/test_fee_calculation.py

def test_fee_calculation_endpoint(client):
    """
    Test that the fee calculation endpoint '/calculate-fee/' computes the delivery fee correctly.
    Formula: base_fee (5.00) + (1.50 * distance_km) + (0.50 * weight_kg)
    Payload: {"distance_km": 10.5, "weight_kg": 2.0}
    Expected: 5.00 + (1.50 * 10.5) + (0.50 * 2.0) = 5.00 + 15.75 + 1.00 = 21.75
    """
    payload = {
        "distance_km": 10.5,
        "weight_kg": 2.0,
    }
    response = client.post("/calculate-fee/", json=payload)
    assert response.status_code == 200
    assert "delivery_fee" in response.json()
    assert response.json()["delivery_fee"] == 21.75
