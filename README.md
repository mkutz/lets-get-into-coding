# Let's get Into Coding

USB Stick Content
- [Python Installer](https://www.python.org/downloads/)
- Zipped venv with all dependencies per OS
   - see [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/#copy-or-link-your-executables)
- [VS Code Installer](https://code.visualstudio.com/download)
- [Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Documentation](https://docs.python.org/3/archives/python-3.11.3-docs-html.zip)
- [Requests Documentation](https://requests.readthedocs.io/_/downloads/en/latest/htmlzip/)
- [Assets for exercises](https://github.com/mkutz/lets-get-into-coding)


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

### 1. Install the Tools

We will use Python as the programming language and VS Code as the IDE/Editor in this course.

Both are quite popular tools, used by many developers.
Having them setup will help you go further in getting into coding.

1. Login to [AgileTD Zone Slack](https://www.agiletd.zone/join-slack) and join the channel [`#lets-get-into-coding`](https://agiletdzone.slack.com/archives/C057371D6AK)
   
2. Follow [instructions to setup Python](https://realpython.com/installing-python/)
   
3. Setup VS Code: [Linux](https://code.visualstudio.com/docs/setup/linux), [MacOS](https://code.visualstudio.com/docs/setup/mac), [Windows](https://code.visualstudio.com/docs/setup/windows)


### Initialize the Environment

1. Create a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) in this project directory:

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


## Objectives

### 1. Check Your Setup

1. Open [hello-wold.py](hello-world.py) in VS Code and understand its content.\
   Feel free to ask any questions you might have!

2. Open a termin in VS code (Menu: Terminal → New Terminal).\
   It should appear at the lower end of the VS code window.

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

- [argument passing](https://docs.python.org/3/tutorial/interpreter.html#argument-passing),
  [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)
- [lists](https://docs.python.org/3/tutorial/introduction.html#lists),
  [sequence types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range),
  [len](https://docs.python.org/3/library/functions.html#len)
- [`if`/`else` statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [`print`](https://docs.python.org/3/library/functions.html#print)
- [strings](https://docs.python.org/3/tutorial/introduction.html#strings),
  [Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

1. Copy [hello-wold.py](hello-world.py) to a new file [hello-you.py](hello-you.py)
   
   ```bash
   cp hello-world.py hello-you.py
   ```

2. Change the code to take an argument, which is printed instead of "World".

   E.g. for `python hello-you.py "Agile Testing Days"` it should print

   ```plain
   Hello Agile Testing Days!
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

- [making requests](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request)
  with [json response content](https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content)
- [`for` statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
  [`for` statement reference](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)

1. Start the train reservation service by running
  
   ```bash
   python train_reservation/main.py
   ```

   This will start a simple train reservation service with in-memory data, using port 8080.

   See [the service's README.md](train_reservation/README.md) if you run in any problems.

2. Create a new file [request-trains.py](request-trains.py).

3. Add code to [list all available trains](train_reservation/README.md#list-all-available-trains) and print them in the following format:
   
   ```plain
   🚆 local_1000
   🚆 express_2000
   ```


### 4. Print Available Seats in Train

Content:

- [dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [`filter` function](https://docs.python.org/3/library/functions.html#filter) (optional)

1. Create a new file [request-available-seats.py](request-available-seats.py).

2. Take a train's name as an argument (e.g. `python request-available-seats.py "local_1000"`).
   
   Make sure the train name is valid.
   Print an error message if it is not.

   E.g. `python request-available-seats.py "unknown_3000"` should return something like

   ```plain
   🚆 unknown_3000 is unknown!
   ```

3. Now [get the details of the requested train](train_reservation/README.md#get-train-details) and extract the seats.

4. Print all seat numbers which are still available (have a empty `booking_reference`).
   
   E.g. `python request-available-seats.py "express_2000"` should return something like

   ```plain
   💺 1A 🔴
   💺 2A 🟢
   💺 3A 🟢
   💺 4A 🟢
   💺 5A 🟢
   💺 6A 🟢
   💺 7A 🟢
   💺 8A 🟢
   💺 1B 🟢
   💺 2B 🔴
   💺 3B 🟢
   💺 4B 🟢
   💺 5B 🟢
   💺 6B 🟢
   💺 7B 🟢
   💺 8B 🟢
   ```


### Reserve a Seat

Content:

- [making post requests](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request)
- [setting request headers](https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers)

1. Create a new file [request-reservation.py](request-reservation.py).
   
2. Add a parameter for the seat you want to reserve.

   E.g. to reserve seat "6B" on train "local_1000", we want to use `python request-reservation.py local_1000 6B`

3. Again, check the inputs to be valid and print error messages if they aren't.

4. Reserve the requested seat by
   
   1. [getting a booking reference](train_reservation/README.md#get-a-booking-reference), and
   
   2. [posting the booking reference](train_reservation/README.md#book-a-seat) in a JSON object like

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

   E.g. print

   ```plain
   🚆 local_1000 💺 2C 🎫 1234567a1
   ```


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


## Resources

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Learn Python in Y minutes](https://learnxinyminutes.com/docs/python/)
- [Requests library docs](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Python docs](https://docs.python.org/), especially
  - [The Python Tutorial](https://docs.python.org/tutorial/)
  - [The Python Standard Library](https://docs.python.org/library/)