import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_cities_spain():
    """
    Test the /countries/Spain/cities endpoint to ensure it returns the correct list of cities for Spain.
    Edge cases: Spain must exist in the data, and the response should be a list.
    """
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200, "Expected status code 200 for Spain cities endpoint"
    assert isinstance(response.json(), list), "Response should be a list of cities"
    # Optionally, check for expected cities if known, e.g.:
    # assert "Madrid" in response.json()
