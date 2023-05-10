# Let's get Into Coding

Ideas: https://automatetheboringstuff.com/


- [ ] Setup: IDE, Tools
  - [ ] [PyCharm](https://www.jetbrains.com/pycharm/)
  - [ ] [Mu](https://codewith.mu/en/download)
  - [ ] [VS Code](https://code.visualstudio.com/)
  - [X] ~~Git?~~ takes too much time
  - [ ] Fallback: https://www.online-python.com/, GitPod
- [ ] Content
  - [ ] Experience the power of coding and how it can help you with your daily work.
  - [ ] Learn the basics of a scripting language (_Python_) to get your coding journey started.
  - [ ] Create your very first self-built tool custom-fit to your recurring tasks.
  - [ ] Join a community of fellow learners to keep you going.
- [ ] Objectives
  1. Setup environment (IDE, Python 3, Shell (?))\
     Have a fallback!
  2. GET request (e.g. https://restful-booker.herokuapp.com/apidoc/index.html#api-Ping-Ping) (watch/do Stefan & Micha)
  3. Parse info from response/local file (JSON, XML) (all, do yourself)
  4. Create a JSON file
  5. POST request (e.g. https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-CreateBooking)
- [ ] Presentation
  - Setup
  - Objectives (incl. "Cheat Sheets")
  - Further reading, Slack channel, etc.


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

We will use Python as the programming language and CS Code as the IDE/Editor in this course.

Both are quite popular tools, used by many developers.
Having them setup will help you go further in getting into coding.

1. Login to Slack and join the channel `#`
2. Follow [instructions to setup Python](https://realpython.com/installing-python/)
3. Setup VS Code: [Linux](https://code.visualstudio.com/docs/setup/linux), [MacOS](https://code.visualstudio.com/docs/setup/mac), [Windows](https://code.visualstudio.com/docs/setup/windows)


## Install Dependencies

1. Create a virtual environment in this project directory:

```shell script
python3 -m venv venv --upgrade-deps
```

2. Activate the virtual environment:

```shell script
source venv/bin/activate
```

3. Install required packages:

```shell script
pip install -r requirements.txt
```

## Train Reservation Service


### Start the Services

```bash
python train_reservation/main.py
```

This will start a simple train reservation service with in-memory data, using port 8080.
You can use a different port if needed via the command line option `--port <custom_port>`


### Using the Service

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


### 2. Perform Your First Request

1. Create a new file `request-booking-ids.py`.
2. …


# Ideas and Notes

## Train Reservation Service

- Create a script that creates some random bookings
- Add support for POST /train-data/reset to reset all train data
- Use train_data_service.py for code reading?
- Possible excersies
  - print a list of the train IDs of all available trains
  - print a list which for each train lists all reserved seats
  - print a list which for each train lists the persentage of reserved seats per coach, and for the whole train
  - create a script that books a specific seat on a specific train
  - create a script that books a specified number of seats in a specified train
  - Add some [business rules](https://github.com/emilybache/KataTrainReservation#business-rules-around-reservations):
    - All seats must be in the same coach
    - At most 70 % of the seats of a given train may be reserved
    - If possible, only 70 % of the seats of a coach should be reserved 
