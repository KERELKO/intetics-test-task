FROM python:3.12-slim AS builder

WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PYTHONPATH=/app/src/

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry==2.1

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false --local && \
    poetry install --only main --no-interaction --no-ansi --no-root

COPY . /app/

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:fastapi_app_factory", "--factory", "--port", "8000", "--host", "0.0.0.0"]
