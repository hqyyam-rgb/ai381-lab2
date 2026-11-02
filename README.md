
AI381 Lab 2 — Bring Your Own Model: Container + CI

This project provides a machine learning API for customer churn prediction using FastAPI, Docker, pytest, and GitHub Actions.

Repository

GitHub: https://github.com/hqyyam-rgb/ai381-lab2

Features

- Loads a trained machine learning model from "model.joblib".
- Provides a health check endpoint.
- Predicts customer churn probability.
- Validates input data using Pydantic.
- Includes automated tests with pytest.
- Uses Docker to package the application.
- Runs automated checks through GitHub Actions.

API Endpoints

Method| Endpoint| Description
GET| "/health"| Checks application and model status
POST| "/predict"| Returns the predicted churn probability

Interactive API documentation is available at "/docs" when the application is running.

Run with Docker

Build the image:

docker build -t ai381-lab2 .

Run the container:

docker run --rm -p 8000:8000 ai381-lab2

Open the API documentation:

http://localhost:8000/docs

Check the health endpoint:

http://localhost:8000/health

Run Tests

Install the project dependencies:

python -m pip install -r requirements.txt

Run the tests:

python -m pytest -v

Run the linter:

ruff check src tests

Container Image

GitHub Container Registry (GHCR):

"ghcr.io/hqyyam-rgb/ai381-lab2/ai381-lab2"

Latest recorded image digest:

sha256:22d6eb4af39108863cdb4ff92560f19e91d8d54eb1a86603c7dc5dc41680b9ec

Continuous Integration

GitHub Actions automatically runs checks for the project. See the "Actions page" (https://github.com/hqyyam-rgb/ai381-lab2/actions) for workflow results.

Technologies

- Python
- FastAPI
- pandas
- scikit-learn / joblib
- pytest
- Ruff
- Docker
- GitHub Actions
- GitHub Container Registry
