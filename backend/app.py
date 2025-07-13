from flask import Flask, jsonify, request
from flask_cors import CORS
from model import predict_days_to_zero
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = "mock_data.json"

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/prediction", methods=["GET"])
def get_predictions():
    with open("backend/data/data.json", "r") as f:
        data = json.load(f)

    result = []

    for item in data:
        stock_history = item.get("stock_history", [])
        stock_list = [entry["stock"] for entry in stock_history]

        if not stock_list:
            continue

        days_left = predict_days_to_zero(stock_list)

        current_stock = stock_list[-1]
        reorder_level = item.get("reorder_level", 20)

        if days_left <= 2:
            status = "critical"
        elif days_left <= 5:
            status = "warning"
        else:
            status = "good"

        result.append({
            "item_no": item["item-no"],
            "item": item["item"],
            "category": item["category"],
            "current_stock": current_stock,
            "days_left": days_left,
            "status": status,
            "reorder_level": reorder_level
        })

    return jsonify(result)


@app.route("/restock", methods=["POST"])
def restock_item():
    content = request.get_json()
    item_no = content.get("item_no")
    quantity = content.get("quantity")
    date = content.get("date", datetime.today().strftime('%Y-%m-%d'))

    data = load_data()
    updated = False

    for item in data:
        if item["item-no"] == item_no:
            stock_history = item["stock_history"]
            if stock_history and stock_history[-1]["date"] == date:
                stock_history[-1]["stock"] += quantity
            else:
                stock_history.append({"date": date, "stock": quantity})
            updated = True
            break

    if updated:
        save_data(data)
        return jsonify({"message": f"Restocked {quantity} units to item {item_no}"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404


@app.route("/daily_update", methods=["POST"])
def update_daily_stock():
    content = request.get_json()
    item_no = content.get("item_no")
    stock = content.get("stock")
    date = content.get("date", datetime.today().strftime('%Y-%m-%d'))

    data = load_data()
    updated = False

    for item in data:
        if item["item-no"] == item_no:
            stock_history = item["stock_history"]
            if stock_history and stock_history[-1]["date"] == date:
                stock_history[-1]["stock"] = stock
            else:
                stock_history.append({"date": date, "stock": stock})
            updated = True
            break

    if updated:
        save_data(data)
        return jsonify({"message": f"Updated stock for {item_no} to {stock} on {date}"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route("/")
def home():
    return "Smart Inventory Tracker API is running!"
  
if __name__ == "__main__":
    print("Smart Inventory Tracker backend is starting...")
    app.run(debug=True)


