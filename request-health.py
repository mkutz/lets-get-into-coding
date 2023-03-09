#! python3

import requests, sys

response = requests.get("https://restful-booker.herokuapp.com/ping")

response.raise_for_status

if response.status_code != 201:
    print("👎")
    sys.exit(1)

print("👍")
sys.exit(0)
