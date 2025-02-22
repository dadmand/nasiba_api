# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${POETRY_HOME}/bin:$PATH"

# Copy just pyproject.toml first
COPY pyproject.toml ./

# Generate poetry.lock & install dependencies
RUN poetry lock && poetry install --no-root --no-dev

# Copy project files
COPY . .

# Expose port
EXPOSE 8888

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888", "--proxy-headers"]