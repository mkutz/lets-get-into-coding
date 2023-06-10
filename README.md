# Let's get Into Coding

## Agenda

| Time  | What                                                                                                                          |
| ----- | ----------------------------------------------------------------------------------------------------------------------------- |
| 10:45 | Welcome, introduction, pair/team up                                                                                           |
| 10:50 | Together: [setup](#setup): [install tools](#1-install-the-tools), [initialize the environment](#2-initialize-the-environment) |
| 11:10 | Together: [check setup](#1-check-your-setup) + [add parameters](#2-add-parameters)                                            |
| 11:20 | In pairs/teams: [return all trains](#3-return-all-trains) + [print available seats](#4-print-available-seats-in-train)        |
| 11:55 | Short check point                                                                                                             |
| 12:00 | In pairs/teams: [reserve a seat](#5-reserve-a-seat) + [further ideas](#further-ideas) or own ideas                            |
| 12:25 | Debrief, collect feedback, encourage to go on and find help on Slack                                                          |


## Setup

### 1. Install the Tools

We will use Python as the programming language and VS Code as the IDE/Editor in this course.

Both are quite popular tools, used by many developers.
Having them setup will help you go further in getting into coding.

1. Login to [AgileTD Zone Slack](https://www.agiletd.zone/join-slack) and join the channel [`#lets-get-into-coding`](https://agiletdzone.slack.com/archives/C057371D6AK)
   
2. Follow [instructions to setup Python](https://realpython.com/installing-python/)
   
3. Setup VS Code: [Linux](https://code.visualstudio.com/docs/setup/linux), [MacOS](https://code.visualstudio.com/docs/setup/mac), [Windows](https://code.visualstudio.com/docs/setup/windows)


### 2. Initialize the Environment

1. Clone this repo and create a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) in the cloned directory:

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

Content:

- [`print`](docs/python-3.11.4-docs-html/library/functions.html#print)


1. Open [1-hello-wold.py](1-hello-world.py) in VS Code and understand its content.\
   Feel free to ask any questions you might have!

2. Open a termin in VS code (Menu: Terminal → New Terminal).\
   It should appear at the lower end of the VS code window.

3. Enter the following in the terminal:

   ```bash
   python 1-hello-world.py
   ```
  
   The output should be

   ```plain
   Hello World!
   ```

  Please ask for help if it doesn't work.


### 2. Add Parameters

Content:

- [argument passing](docs/python-3.11.4-docs-html/tutorial/interpreter.html#argument-passing),
  [sys.argv](docs/python-3.11.4-docs-html/library/sys.html#sys.argv)
- [`print`](docs/python-3.11.4-docs-html/library/functions.html#print)
- [strings](docs/python-3.11.4-docs-html/tutorial/introduction.html#strings),
  optinally [formatted string literals](docs/python-3.11.4-docs-html/reference/lexical_analysis.html#f-strings)
- [lists](docs/python-3.11.4-docs-html/tutorial/introduction.html#lists),
  [sequence types](docs/python-3.11.4-docs-html/library/stdtypes.html#sequence-types-list-tuple-range),
  [len](docs/python-3.11.4-docs-html/library/functions.html#len)
- [`if`/`else` statements](docs/python-3.11.4-docs-html/tutorial/controlflow.html#if-statements)

1. Open [2-hello-you.py](2-hello-you.py).

2. Change the code to take an argument, which is printed instead of "World".

   E.g. for `python 2-hello-you.py "AgileTD"` it should print

   ```plain
   Hello AgileTD!
   ```

3. If no argument is given (`python 2-hello-you.py`), print

   ```plain
   Hello you!
   ```

4. If more then one argument is given (e.g. `python 2-hello-you.py Stefan Micha`), print
   
   ```plain
   Hello Stefan and Micha!
   ```


### 3. Return all Trains

Content:

- [making requests](docs/requests-latest/index.html#make-a-request)
  with [json response content](docs/requests-latest/index.html#json-response-content)
- [`for` statements](docs/python-3.11.4-docs-html/tutorial/controlflow.html#for-statements)
  [`for` statement reference](docs/python-3.11.4-docs-html/reference/compound_stmts.html#the-for-statement)

1. Start the train reservation service by running
  
   ```bash
   python train_reservation/main.py
   ```

   This will start a simple train reservation service with in-memory data, using port 8080.

   See [the service's README.md](train_reservation/README.md) if you run in any problems.

2. Open [3-request-trains.py](3-request-trains.py).

3. Add code to [list all available trains](train_reservation/README.md#list-all-available-trains) and print them in the following format:
   
   ```plain
   🚆 local_1000
   🚆 express_2000
   ```


### 4. Print Available Seats in Train

Content:

- [dictionaries](docs/python-3.11.4-docs-html/library/stdtypes.html#mapping-types-dict)
- [`filter` function](docs/python-3.11.4-docs-html/library/functions.html#filter) (optional)

1. Open [4-request-available-seats.py](4-request-available-seats.py).

2. Take a train's name as an argument (e.g. `python 4-request-available-seats.py "local_1000"`).
   
   Make sure the train name is valid.
   Print an error message if it is not.

   E.g. `python 4-request-available-seats.py "unknown_3000"` should return something like

   ```plain
   🚆 unknown_3000 is unknown!
   ```

3. Now [get the details of the requested train](train_reservation/README.md#get-train-details) and extract the seats.

4. Print all seat numbers which are still available (have a empty `booking_reference`).
   
   E.g. `python 4-request-available-seats.py "express_2000"` should return something like

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


### 5. Reserve a Seat

Content:

- [making post requests](docs/requests-latest/index.html#make-a-request)
- [setting request headers](docs/requests-latest/index.html#custom-headers)

1. Open [5-request-reservation.py](5-request-reservation.py).
   
2. Add a parameter for the seat you want to reserve.

   E.g. to reserve seat "6B" on train "local_1000", we want to use `python 5-request-reservation.py local_1000 6B`

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


### Further Ideas

- Create a script that creates some random bookings
- Use functions to structure your scripts (e.g. `verify_train_id(train_id)`, `book_seat(train_id, seat_number)`)
- Create a reservation script that asks for train_id and seat_number, instead of using call parameters
- Print a list which for each train lists the percentage of reserved seats per coach, and for the whole train
- Create a script that books a specified number of seats in a specified train
- Use [train_data_service](train_reservation/train_data_service.py) for code reading
- Add support for POST /train-data/reset to [train_data_service](train_reservation/train_data_service.py), resetting all train data


## Resources

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Learn Python in Y minutes](https://learnxinyminutes.com/docs/python/)
- [Requests library docs](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Python docs](https://docs.python.org/), especially
  - [The Python Tutorial](https://docs.python.org/tutorial/)
  - [The Python Standard Library](https://docs.python.org/library/)