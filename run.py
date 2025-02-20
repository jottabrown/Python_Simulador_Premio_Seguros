#---------------------------------------------------------------------------------------
# Author: Jean Alves
# Position: Systems Analyst | Software Engineer | Machine Learning Engineer
# Email: jeancleber.alves@hotmail.com
# LinkedIn: https://www.linkedin.com/in/jean-alves-6671a7105/
#---------------------------------------------------------------------------------------

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate_premium():
    response = client.post("/calculate", json={
        "make": "Toyota",
        "model": "Corolla",
        "year": 2015,
        "value": 100000.0,
        "deductible_percentage": 0.1,
        "broker_fee": 50.0
    })
    print(f"Status Code: {response.status_code}")
    print(f"Response Data: {response.json()}")
    assert response.status_code == 200
    data = response.json()
    assert "final_premium" in data

if __name__ == "__main__":
    test_calculate_premium()
    print("Test completed successfully!")
