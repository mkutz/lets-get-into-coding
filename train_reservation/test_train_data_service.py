import json

import cherrypy
from cherrypy.test import helper

from train_reservation.train_data_service import TrainDataService


class TrainDataServiceTest(helper.CPWebCase):
    def post(self, url, body):
        self.getPage(
            url=url,
            method="POST",
            headers=[
                ("Content-Type", "application/json"),
                ("Content-Length", str(len(body))),
            ],
            body=body,
        )


class EmptyTrainTest(TrainDataServiceTest):
    @staticmethod
    def setup_server():
        train_data = json.dumps(
            {"test_train": {"seats": {"1A": {"coach": "A", "seat_number": "1", "booking_reference": "", }}}})
        cherrypy.tree.mount(TrainDataService(train_data))

    def test_fetch_train_data(self):
        self.getPage("/trains/test_train")
        self.assertStatus(200)
        self.assertInBody("1A")

    def test_get_data_for_unknown_train_returns_404(self):
        self.getPage("/trains/unknown_train")
        self.assertStatus(404)

    def test_reserve_seat(self):
        self.post(
            "/reserve",
            json.dumps(
                {
                    "train_id": "test_train",
                    "seats": ["1A"],
                    "booking_reference": "01234567",
                }
            ),
        )
        self.assertStatus(200)
        self.assertInBody('"booking_reference": "01234567"')

    def test_reserve_seat_with_unknown_train_returns_400(self):
        self.post(
            "/reserve",
            json.dumps(
                {
                    "train_id": "unknown_train",
                    "seats": ["1A"],
                    "booking_reference": "01234567",
                }
            ),
        )
        self.assertStatus(400)
        self.assertInBody("Train not found: unknown_train.")

    def test_reserve_seat_with_unknown_seat_returns_400(self):
        self.post(
            "/reserve",
            json.dumps(
                {
                    "train_id": "test_train",
                    "seats": ["XX"],
                    "booking_reference": "01234567",
                }
            ),
        )
        self.assertStatus(400)
        self.assertInBody("Seat not found: XX.")


class ReservedTrainTest(TrainDataServiceTest):
    @staticmethod
    def setup_server():
        train_data = json.dumps(
            {"test_train": {"seats": {"1A": {"coach": "A", "seat_number": "1", "booking_reference": "existing", }}}})
        cherrypy.tree.mount(TrainDataService(train_data))

    def test_reserve_seat_when_already_reserved(self):
        self.post(
            "/reserve",
            json.dumps(
                {
                    "train_id": "test_train",
                    "seats": ["1A"],
                    "booking_reference": "01234567",
                }
            ),
        )
        self.assertStatus(200)
        self.assertInBody("Already booked with reference: existing.")

        self.getPage("/trains/test_train")
        self.assertStatus(200)
        self.assertInBody('"booking_reference": "existing"')

    def test_reset(self):
        self.post("/reset/test_train", json.dumps({}))
        self.assertStatus(200)
        self.assertNotInBody("existing")

    def test_reset_unknown(self):
        self.post("/reset/unknown_train", json.dumps({}))
        self.assertStatus(404)

    def test_reset_get(self):
        self.getPage("/reset/test_train")
        self.assertStatus(405)
