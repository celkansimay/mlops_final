from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ["Modele hoşgeldiniz."]

def test_model():
    test_data = {
        "CreditScore": 0,
        "Geography": "france",
        "Gender": "female",
        "Age": 0,
        "Tenure": 0,
        "Balance": 1500,
        "NumOfProducts": 2,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 50000.0
    }


    response = client.post("/predict/model", json=test_data)


    assert response.status_code == 200
    assert "predict" in response.json()
    assert isinstance(response.json()["predict"], int)