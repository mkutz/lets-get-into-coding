import requests

response = requests.get("http://127.0.0.1:8080/booking-reference")
response.raise_for_status()

print(f"Got booking reference {response.text}")
