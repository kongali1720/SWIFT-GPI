from fastapi.testclient import TestClient
from mock_tracker import app

client = TestClient(app)

def test_create_payment():
    response = client.post("/payments", json={
        "uetr": "12345",
        "amount": 500,
        "currency": "USD",
        "sender": "BANKUS33XXX",
        "receiver": "BNINIDJAXXX"
    })
    assert response.status_code == 200
    assert response.json()["amount"] == 500
