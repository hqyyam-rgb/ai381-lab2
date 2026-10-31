# AI381 Lab 2 — Container and CI

[![AI381 Lab 2 CI](https://github.com/hqyyam-rgb/ai381-lab2/actions/workflows/ci.yml/badge.svg)](https://github.com/hqyyam-rgb/ai381-lab2/actions/workflows/ci.yml)

Course: AI381 Machine Learning Operations  
University: Jordan University of Science and Technology (JUST)  
Semester: Fall 2026/27

## Project Overview

This project packages a machine learning churn prediction model into a FastAPI application and runs it inside a Docker container.

The project includes automated testing, code linting, Docker image security scanning with Trivy, and publishing the image to GitHub Container Registry (GHCR).

## Features

- FastAPI REST API for churn prediction.
- /health endpoint to check application and model status.
- /predict endpoint to return churn probability.
- Input validation using Pydantic.
- Automated tests using pytest.
- Code linting using Ruff.
- Multi-stage Docker build.
- Non-root user inside the container.
- Docker health check.
- GitHub Actions CI workflow.
- Trivy vulnerability scanning.
- Docker image published to GHCR using a commit SHA tag.

## Project Structure

.
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── app/
│   │   └── main.py
│   └── train/
│       └── train.py
├── tests/
│   └── test_api.py
├── Dockerfile
├── requirements.txt
├── model.joblib
├── churn_v2.csv
└── README.md
## Run Locally

Install the dependencies:

python -m pip install -r requirements.txt
python -m pip install ruff pytest
Run the tests and lint checks:

python -m pytest -v
python -m ruff check src tests
Start the API:

uvicorn src.app.main:app --host 0.0.0.0 --port 8000
Check the health endpoint:

curl http://localhost:8000/health
## Run with Docker

Build the image:

docker build -t ai381-lab2 .
Run the container:

docker run --rm -p 8000:8000 ai381-lab2
In another terminal, check the health endpoint:

curl http://localhost:8000/health
## Prediction Endpoint

Send a prediction request:

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"tenure_months":12,"monthly_fee":75.5,"contract":"Month-to-month","internet_service":"Fiber optic","support_calls":2}'
The API returns a churn probability.

## Continuous Integration

GitHub Actions runs linting and automated tests, builds the Docker image, scans it with Trivy, and publishes the image to GHCR on pushes to the configured branches.

## Container Image

GHCR image:

ghcr.io/hqyyam-rgb/ai381-lab2/ai381-lab2

Published tag:

793d27960fa9492b7d78d276c4de6f08ca2145f9

Image digest:

sha256:a8ecea79d4219cfef7fd1a1840528badee6521f6cab531737d633a8971d2d344

## Repository

https://github.com/hqyyam-rgb/ai381-lab2
