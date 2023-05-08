"""
Implementation of Train Data Service.
"""

import json
import pathlib

import cherrypy


class TrainDataService:
    def __init__(self, json_data):
        self.train_data = json.loads(json_data)

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def trains(self, train_id=""):
        if train_id == "":
            return list(self.train_data.keys())
        with cherrypy.HTTPError.handle(KeyError, 404):
            return self.train_data[train_id]

    @cherrypy.expose()
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def reserve(self):
        reservation = cherrypy.request.json
        train_id = reservation["train_id"]
        seats = reservation["seats"]
        booking_reference = reservation["booking_reference"]

        with cherrypy.HTTPError.handle(KeyError, 400, f"Train not found: {train_id}."):
            train = self.train_data[train_id]

        for seat in seats:
            with cherrypy.HTTPError.handle(KeyError, 400, f"Seat not found: {seat}."):
                existing_booking_reference = train["seats"][seat]["booking_reference"]

            if (
                existing_booking_reference
                and existing_booking_reference != booking_reference
            ):
                return f"Already booked with reference: {existing_booking_reference}."

        for seat in seats:
            train["seats"][seat]["booking_reference"] = booking_reference

        return self.trains(train_id)

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def reset(self, train_id):
        if cherrypy.request.method != "POST":
            raise cherrypy.HTTPError(405, 'Method Not Allowed')

        with cherrypy.HTTPError.handle(KeyError, 404):
            train = self.train_data[train_id]

        for seat in train["seats"].values():
            seat["booking_reference"] = ""

        return self.trains(train_id)


if __name__ == "__main__":
    script_dir = pathlib.Path(__file__).parent.resolve()
    with open(f"{script_dir}/trains.json") as f:
        train_data = f.read()
    cherrypy.quickstart(TrainDataService(train_data))
