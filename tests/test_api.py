from fastapi.testclient import TestClient

from src.app.main import app, model

client = TestClient(app)

VALID_CUSTOMER = {
    "tenure_months": 12,
    "monthly_fee": 75.5,
    "contract": "Month-to-month",
    "internet_service": "Fiber optic",
    "support_calls": 2,
}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_model_is_loaded():
    assert model is not None


def test_prediction_returns_probability():
    response = client.post("/predict", json=VALID_CUSTOMER)
    assert response.status_code == 200
    assert "churn_probability" in response.json()


def test_invalid_input_is_rejected():
    customer = VALID_CUSTOMER.copy()
    customer["tenure_months"] = -1

    response = client.post("/predict", json=customer)
    assert response.status_code == 422


def test_prediction_is_deterministic():
    first = client.post("/predict", json=VALID_CUSTOMER)
    second = client.post("/predict", json=VALID_CUSTOMER)

    assert first.status_code == 200
    assert second.status_code == 200
    assert (
        first.json()["churn_probability"]
        == second.json()["churn_probability"]
    )