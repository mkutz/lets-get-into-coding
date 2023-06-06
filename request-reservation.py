#! python3

import sys, requests

if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <train_name> <seat_number>\n" % sys.argv[0])
    sys.exit(1)

requested_train_id = sys.argv[1]
requested_seat_number = sys.argv[2]

train_response = requests.get("http://127.0.0.1:8080/train-data/trains/%s" % requested_train_id)
if train_response.status_code == 404:
    sys.stderr.write("🚆 %s is unknown!\n" % requested_train_id)
    sys.exit(2)
train_response.raise_for_status()

seats = train_response.json()["seats"]
for number, seat in seats.items():
    if number == requested_seat_number:
        if seat["booking_reference"] != "":
            sys.stderr.write("🚆 %s 💺 %s is not available!\n" % (requested_train_id, requested_seat_number))
            sys.exit(3)
        
        booking_reference_response = requests.get("http://127.0.0.1:8080/booking-reference/")
        booking_reference = booking_reference_response.text

        reservation_response = requests.post("http://127.0.0.1:8080/train-data/reserve",
                      json={"train_id": requested_train_id, "seats": [requested_seat_number], "booking_reference": booking_reference},
                      headers={"content-type": "application/json"})
        
        reservation_response.raise_for_status()
        
        print("🚆 %s 💺 %s 🎫 %s" % (requested_train_id, requested_seat_number, booking_reference))
        sys.exit(0)

sys.stderr.write("🚆 %s 💺 %s is invalid!\n" % (requested_train_id, requested_seat_number))
sys.exit(4)
