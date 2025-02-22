-- Install dependencies
pip install -r requirements.txt

-- Run tests
pytest tests/

-- RUN
uvicorn app.main:app --reload --host 0.0.0.0 --port 8888

-- Docker compose
docker compose up --build
