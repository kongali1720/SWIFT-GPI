from fastapi import FastAPI
import uuid

app = FastAPI()

# In-memory database (can be replaced with Postgres/MySQL)
transactions = {}

@app.post("/initiate-payment/")
def initiate_payment(amount: float, sender: str, receiver: str):
    uetr = str(uuid.uuid4())
    transactions[uetr] = {"amount": amount, "sender": sender, "receiver": receiver, "status": "Received"}
    return {"UETR": uetr, "status": transactions[uetr]}

@app.post("/update-status/{uetr}")
def update_status(uetr: str, status: str):
    if uetr in transactions:
        transactions[uetr]["status"] = status
        return {"UETR": uetr, "status": status}
    return {"error": "Transaction not found"}

@app.get("/track/{uetr}")
def track_payment(uetr: str):
    if uetr in transactions:
        return {"UETR": uetr, "details": transactions[uetr]}
    return {"error": "Transaction not found"}
