import pathlib

import cherrypy
import click

from booking_reference_service import BookingReferenceService
from train_data_service import TrainDataService


@click.command()
@click.option("--port", default=8080, help="port")
def main(port):
    script_dir = pathlib.Path(__file__).parent.resolve()
    with open(f"{script_dir}/trains.json") as file:
        train_data = file.read()

    cherrypy.config.update(
        {"server.socket_port": port, "server.socket_host": "0.0.0.0"}
    )
    cherrypy.tree.mount(BookingReferenceService(123456789), "/booking-reference")
    cherrypy.tree.mount(TrainDataService(train_data), "/train-data")
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    main()
