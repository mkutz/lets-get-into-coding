# Train Reservation Service

This service is a very simple version of an API-based trains seat reservation system.
It is based on the [Train Reserviation Kata](https://github.com/emilybache/KataTrainReservation) by [Emily Bache](http://bacheconsulting.com/).
It uses static data and will reset its state when shut down.


## Starting the Service

You can start the service via

```bash
python main.py
```

Accept if your system might ask you to allow external connections.

This will start a simple train reservation service with in-memory data, using port 8080.

<details>
<summary>
    If you get the error <code>cherrypy.process.wspbus.ChannelFailures: Timeout('Port 8080 not free on 0.0.0.0.')</code>
</summary>

```log
ENGINE Shutting down due to error in start listener:
Traceback (most recent call last):
    File "/Users/Michael.Kutz/Projects/lets-get-into-coding/venv/lib/python3.11/site-packages/cherrypy/process/wspbus.py", line 268, in start
    self.publish('start')
    File "/Users/Michael.Kutz/Projects/lets-get-into-coding/venv/lib/python3.11/site-packages/cherrypy/process/wspbus.py", line 248, in publish
    raise exc
cherrypy.process.wspbus.ChannelFailures: Timeout('Port 8080 not free on 0.0.0.0.')
```

you can use a different port if needed via the command line option `--port <custom_port>`. E.g.

```bash
python train_reservation/main.py --port 9090
```
</details>


## Stopping the Service

You can stop the service by pressing <kbd>^</kbd> + <kbd>C</kbd> on MacOS or <kbd>Ctrl</kbd> + <kbd>C</kbd> in the terminal it runs in.


## Using the Service

### List All Available Trains

```bash
curl http://127.0.0.1:8080/train-data/trains
```

Will return a JSON list of all trains' IDs.

<details>
<summary>
JSON?
</summary>
The <a href="https://en.wikipedia.org/wiki/JSON">JavaScript Object Notation (JSON)</a> is often used as a human readable/writable format in APIs.
</details>

E.g.:

```json
["local_1000", "express_2000"]
```


### Get Train Details

```bash
curl http://127.0.0.1:8080/train-data/trains/:train_id
```

E.g. get the details on "express_2000":

```bash
curl http://127.0.0.1:8080/train-data/trains/express_2000
```


### Get a Booking Reference

```bash
curl http://127.0.0.1:8080/booking-reference/
```


### Book a Seat

```bash
curl http://127.0.0.1:8080/train-data/reserve \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"train_id": "<train_id>", "seats": <seat_numbers>, "booking_reference": "<booking_reference>"}'
```

E.g. to book seat "1A" and "2B" on train "express_2000" under reference "12345":

```bash
curl http://127.0.0.1:8080/train-data/reserve \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"train_id": "express_2000", "seats": ["1A", "2B"], "booking_reference": "12345"}'
```


### Remove all Seat Reservations

```bash
curl http://127.0.0.1:8080/train-data/reset/:train_id \
  --request POST
```

E.g. remove all reservations on train "express_2000":

```bash
curl http://127.0.0.1:8080/train-data/reset/express_2000 \
  --request POST
```
