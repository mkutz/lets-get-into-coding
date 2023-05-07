import cherrypy
import itertools


class BookingReferenceService:
    def __init__(self, starting_point):
        self.counter = itertools.count(int(str(starting_point), 16) + 1)

    @cherrypy.expose()
    def index(self):
        next_number = next(self.counter)
        return str(hex(next_number))[2:]


if __name__ == "__main__":
    cherrypy.quickstart(BookingReferenceService(123456789))
