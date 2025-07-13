import requests

url = "http://127.0.0.1:5000/daily_update"  # Change to /restock if needed

data = {
    "item_no": "001",
    "stock": 160,
    "date": "2025-07-13"
}

response = requests.post(url, json=data)
print("Status:", response.status_code)
print("Response:", response.json())