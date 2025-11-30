from fastapi import FastAPI, HTTPException
import json
from pathlib import Path

app = FastAPI(title="Pizzeria API")

ORDERS_FILE = Path("orders.json")


def load_orders():
    if not ORDERS_FILE.exists():
        return []
    with open(ORDERS_FILE, "r") as f:
        return json.load(f)

def save_orders(orders):
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=4)


@app.get("/")
def root():
    return {"message": "Welcome to the Pizzeria API!"}


# ---------------------------
# READ – Get a single order
# ---------------------------
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    orders = load_orders()

    for order in orders:
        if order["id"] == order_id:
            return order

    raise HTTPException(status_code=404, detail="Order not found")


# ---------------------------
# READ – Get all orders
# ---------------------------
@app.get("/orders")
def list_orders():
    return load_orders()
