#! python3

import sys, requests

if len(sys.argv) != 2:
    print("Usage: %s <train_name>" % sys.argv[0])
    sys.exit(1)

train = sys.argv[1]
train_response = requests.get("http://127.0.0.1:8080/train-data/trains/%s" % train)
if train_response.status_code == 404:
    print("Train %s is unknown" % train)
    sys.exit(2)
train_response.raise_for_status()

seats = train_response.json()["seats"]
for number, seat in seats.items():
    if seat["booking_reference"] == "":
        print(number)
