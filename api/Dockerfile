FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy project metadata first for better caching
COPY pyproject.toml /app/pyproject.toml

# Install runtime deps directly (includes uvicorn)
RUN pip install --no-cache-dir -U pip \
 && pip install --no-cache-dir \
      "uvicorn[standard]" \
      fastapi \
      sqlalchemy \
      "psycopg[binary]" \
      alembic \
      pydantic \
      pydantic-settings \
      httpx \
      redis

# Now copy the app code
COPY . /app

EXPOSE 8000
