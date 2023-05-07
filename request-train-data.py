import requests, json

train_id = "express_2000"

response = requests.get(f"http://127.0.0.1:8080/train-data/trains/{train_id}")
response.raise_for_status()

train_data = json.loads(response.text)

print(f"Got train data for {train_id}:")
print()
print(json.dumps(train_data, indent=2))
