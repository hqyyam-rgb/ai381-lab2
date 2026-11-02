from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "model.joblib"

FEATURES = [
    "tenure_months",
    "monthly_fee",
    "contract",
    "internet_service",
    "support_calls",
]

app = FastAPI(title="AI381 Lab 2 Churn API")

model = joblib.load(MODEL_PATH)


class Customer(BaseModel):
    tenure_months: int = Field(ge=0)
    monthly_fee: float = Field(ge=0)
    contract: str
    internet_service: str
    support_calls: int = Field(ge=0)


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict")
def predict(customer: Customer):
    data = customer.model_dump()
    X = pd.DataFrame([data])[FEATURES]
    probability = float(model.predict_proba(X)[0, 1])

    return {"churn_probability": round(probability, 3)}