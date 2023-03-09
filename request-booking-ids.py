#! python3

import requests, json, sys

response = requests.get("https://restful-booker.herokuapp.com/booking")
response.raise_for_status

booking_ids = json.loads(response.text)

print("Found %s bookings" % len(booking_ids))

sys.exit(0)
