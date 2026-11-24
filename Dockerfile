# ---------- Stage 1: Build dependencies and prepare the model ----------
FROM python:3.12.15-slim-trixie AS builder

WORKDIR /build

COPY requirements.txt .

RUN mkdir -p /install
RUN python -m pip install --no-cache-dir --target=/install -r /build/requirements.txt

COPY src/ src/
COPY data/ data/
COPY artifacts/ artifacts/

ARG GIT_SHA=local

RUN if [ -f artifacts/model.joblib ]; then \
        mkdir -p models \
        && cp artifacts/model.joblib artifacts/metadata.json models/ \
        && python -c "import json,sys; p='models/metadata.json'; m=json.load(open(p)); m['model_version']=sys.argv[1][:7]; json.dump(m,open(p,'w'))" "$GIT_SHA"; \
    else \
        GIT_SHA=$GIT_SHA python -m src.train.train; \
    fi

# ---------- Stage 2: Runtime image ----------
FROM python:3.12.15-slim-trixie

LABEL org.opencontainers.image.title="ai381-churn-starter" \
      org.opencontainers.image.description="AI381 Machine Learning Operations churn API starter"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/deps:/app

WORKDIR /app

COPY --from=builder /install /app/deps
COPY --from=builder /build/src ./src
COPY --from=builder /build/models ./models

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]