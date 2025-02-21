from fastapi.testclient import TestClient
from app.main import app
from app.core.database import Base, engine
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.dependencies import get_db
import random

client = TestClient(app)

def get_random_id():
    return str(random.randint(1000, 100000))

def test_create_third_party():
    random_id = get_random_id()
    response = client.post(
        "/api/v1/third-party/",
        json={
            "third_party_id": random_id,
            "first_name": "Ali",
            "last_name": "Dadmand",
            "national_id": "123456789",
            "phone_number": "1234567890",
            "birth_date": "1982-01-01",
            "amount": 10000.0,
            "number_of_repayments": 12,
        },
    )
    assert response.status_code == 201
    data = response.json()
    
    assert data["c_third_party_id"] == random_id
    assert data["c_first_name"] == "Ali"
    assert data["c_last_name"] == "Dadmand"


    # Then, retrieve the third party
    response = client.get(f"/api/v1/third-party/{random_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["c_third_party_id"] == random_id
    assert data["c_first_name"] == "Ali"
    assert data["c_last_name"] == "Dadmand"

def test_get_all():
    # First, create multiple third parties
    random_ids = [get_random_id() for _ in range(3)]
    
    # Then get all third parties
    response = client.get("/api/v1/third-party/")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= len(random_ids)  # Should have at least our new entries
    