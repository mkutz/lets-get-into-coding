# Let's get Into Coding

USB Stick Content
- Python Installer: <https://www.python.org/downloads/>
- VS Code Installer: <https://code.visualstudio.com/download>
- Zipped venv with all dependencies per OS
- Python Extension: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>
- Assets for exercises
- Train Reservation Backend: <https://github.com/rewe-digital-incubator/kata-train-reservation>


## Agenda

10:45 – 12:30

| Time  | What                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------- |
| 10:45 | Welcome, introduction, setup instructions (slides), pairup people without computer, get everyone into Slack channel |
| 11:00 | Hands-on setup together: IDE, Python, Shell                                                                         |
| 11:15 | First task: GET https://restful-booker.herokuapp.com/apidoc/index.html#api-Ping-Ping                                |
| 11:35 | Present instructions for second task along with needed docs: Parse info from response/local file (JSON, XML)        |
| 11:45 | Short break for those who need one (?)                                                                              |
| 12:00 | Present solution for second task                                                                                    |
| 12:10 | Present instructions for further tasks, let everybody work on them                                                  |
| 12:25 | Debrief, collect feedback, encourage to go on and find help on Slack                                                |


## Setup

### Tools

We will use Python as the programming language and CS Code as the IDE/Editor in this course.

Both are quite popular tools, used by many developers.
Having them setup will help you go further in getting into coding.

1. Login to Slack and join the channel `#`
   
2. Follow [instructions to setup Python](https://realpython.com/installing-python/)
   
3. Setup VS Code: [Linux](https://code.visualstudio.com/docs/setup/linux), [MacOS](https://code.visualstudio.com/docs/setup/mac), [Windows](https://code.visualstudio.com/docs/setup/windows)


### Dependencies

1. Create a virtual environment in this project directory:

   ```bash
   python3 -m venv venv --upgrade-deps
   ```

2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. You should now be able to run `python` (without `3`):
   
   ```bash
   python --version
   ```

   Should return something like `Python 3.11.3`.


#### Using the Service

List all available trains:

```bash
curl http://127.0.0.1:8080/train-data/trains
```

Check for free seats on the train "express_2000":

```bash
curl http://127.0.0.1:8080/train-data/trains/express_2000
```

Get a booking reference:

```bash
curl http://127.0.0.1:8080/booking_reference
```

Book a seat:

```bash
curl http://127.0.0.1:8080/train-data/reserve \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"train_id": "express_2000", "seats": ["1A"], "booking_reference": "01234567"}'
```

Remove all seat reservations for train "express_2000":

```bash
curl http://127.0.0.1:8080/train-data/reset/express_2000 \
  --request POST
```

You can stop the service by pressing <kbd>^</kbd> + <kbd>C</kbd> on MacOS or <kbd>Ctrl</kbd> + <kbd>C</kbd>.


## Objectives

### 1. Check Your Setup

1. Open [hello-wold.py](hello-world.py) in VS Code and understand its content.\
   Feel free to ask any questions you might have!

2. Open a termin in VS code (Menu: Terminal → New Terminal).\
   It should at the lower end of the VS code window.

3. Enter the following in the terminal:

   ```bash
   python hello-world.py
   ```
  
   The output should be

   ```plain
   Hello World!
   ```

  Please ask for help if it doesn't work.


### 2. Add Parameters

Content:

- sys.argv
- arrays, len
- if/else
- print
- string interpolation/formatted strings

1. Copy [hello-wold.py](hello-world.py) to a new file [hello-you.py](hello-you.py)
   
   ```bash
   cp hello-world.py hello-you.py
   ```

2. Change the code to take an argument, which is printed instead of "World".

   E.g. for `python hello-you.py "Agile Testing Days"` it should print

   ```plain
   Hello AgileTD!
   ```

3. If no argument is given (`python hello-you.py`), print

   ```plain
   Hello you!
   ```

4. If more then one argument is given (e.g. `python hello-you.py Stefan Micha`), print
   
   ```plain
   Hello Stefan and Micha!
   ```


### 3. Return all Trains

Content:

- requests, json
- for in

1. Start the train reservation service by running
  
   ```bash
   python train_reservation/main.py
   ```

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

2. Create a new file [request-trains.py](request-trains.py).

3. Add code to request all trains (http://127.0.0.1:8080/train-data/trains) and print them in the following format:
   
   ```plain
   🚆 local_1000
   🚆 express_2000
   ```


### 4. Print Available Seats in Train

Content:

- complex dictionaries
- filter (optional)

1. Create a new file [request-available-seats.py](request-available-seats.py).

2. Take a train's name as an argument (e.g. `python request-available-seats.py "local_1000"`).
   
   Make sure the train name is valid. Print an error message if it is not.

   E.g. `python request-available-seats.py "unknown_3000"` should return something like

   ```
   Train unknown_3000 is unknown!
   ```

3. Now filter get the details of the requested train (http://127.0.0.1:8080/train-data/trains/<requested-train>), extract the seats.

4. Print all seat numbers which are still available (have a non-empty `booking_reference`).


### Reserve a Seat

Content:

- post data

1. Create a new file [request-reservation.py](request-reservation.py)
   
2. Add a parameter for the seat you want to reserve.

   E.g. to reserve seat "6B" on train "local_1000", we want to use `python request-reservation.py local_1000 6B`

3. Again, check the inputs to be valid and print error messages if they aren't.

4. Reserve the requested seat by
   
   1. getting a booking reference (http://127.0.0.1:8080/booking_reference), and
   
   2. posting the booking reference (http://127.0.0.1:8080/train-data/reserve) in a JSON object like

      ```json
      {
         "train_id": "<requested_train>",
         "seats": ["<requested_seat>"],
         "booking_reference": "<booking_reference>"
      }
      ```

      E.g.

      ```json
      {
         "train_id": "local_1000",
         "seats": ["6B"],
         "booking_reference": "01234567"
      }
      ```

5. If successful, print the booking reference; otherwise print an error message.


# Ideas and Notes

## Train Reservation Service

- Create a script that creates some random bookings
- Add support for POST /train-data/reset to reset all train data
- Use train_data_service.py for code reading?
- Possible excersies
  - print a list of the train IDs of all available trains
  - print a list which for each train lists all reserved seats
  - print a list which for each train lists the percentage of reserved seats per coach, and for the whole train
  - create a script that books a specific seat on a specific train
  - create a script that books a specified number of seats in a specified train
  - Add some [business rules](https://github.com/emilybache/KataTrainReservation#business-rules-around-reservations):
    - All seats must be in the same coach
    - At most 70 % of the seats of a given train may be reserved
    - If possible, only 70 % of the seats of a coach should be reserved 


## Further Ideas

- https://automatetheboringstuff.com/