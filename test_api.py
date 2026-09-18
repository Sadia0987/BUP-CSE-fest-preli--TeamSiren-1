import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_optimize():
    response = client.post(
        "/optimize",
        json={
            "building_id": "BUP-001",
            "current_load": 100,
            "solar_generation": 40,
            "battery_level": 70
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["recommended_action"] == "Use battery backup"
    assert data["estimated_saving"] == 40


def test_ask():
    response = client.post(
        "/ask",
        json={
            "question": (
                "My building has 100 kW load, "
                "40 kW solar generation and 70% battery"
            )
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["current_load"] == 100
    assert data["solar_generation"] == 40
    assert data["battery_level"] == 70
    assert data["recommended_action"] == "Use battery backup"
    assert data["remaining_load"] == 60


def test_missing_data():
    response = client.post(
        "/ask",
        json={
            "question": "My battery is 70%"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "current load" in data["message"]
    assert "solar generation" in data["message"]
def test_invalid_battery():
    response = client.post(
        "/ask",
        json={
            "question": (
                "My building has 100 kW load, "
                "40 kW solar generation and 150% battery"
            )
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Battery level must be between 0 and 100."
    )