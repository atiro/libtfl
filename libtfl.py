import requests

TFL_API_URL = "https://api.tfl.gov.uk/"

TFL_API_APP_ID = ""
TFL_API_APP_KEY = ""
MY_STOP = ""

class TFLBase:
    type = None
    action = None

    def update():
        pass
        # construct url based on api_url, type, action, and keys


class Stop(TFLBase):
    stop_point = None
    stop_time = None

    def show_arrivals():
        pass


class Transport(TFLBase):
    pass

# Modes of Transport

class Bus(Transport):
    pass

class Tube(Transport):
    pass

class Bike(Transport):
    pass

class Train(Transport):
    pass

class CableCar(Transport):
    pass

class DLR(Transport):
    pass

class Tram(Transport):
    pass

# Transport egress

class Station(Stop):
    pass


class BikePoint(Stop):

    def __init__(self, point=None, bbox=None, locus=None, name=None):
        pass


class BusStop(Stop):
    route = None
    stop = None
    json = None

    route_stops = []
    next_stop = None

    def __init__(self, stop=None, route=None):
        self.stop = stop
        self.route = route
        print("Created route", self.route)

    def update(self):
        self.action = "Arrivals"
        req = requests.get("https://api.tfl.gov.uk/StopPoint/%s/Arrivals?app_id=%s&app_key=%s")
        self.json = req.json()
        self.next_stop = self.json[0]['timeToStation']

    def status(self):
        pass

    def __str__(self):
        return self.route

# Lines/Routes

class Place(Location):
    pass

class Line(Location):
    pass

class Route(Location):
    pass

class Road(Location):
    pass

# Search

class Search(TFLBase):
    pass

class Journey(TFLBase):
    """ Journey Planner Query """
    pass



r22 = BusStop(route="R22", stop=MY_STOP)

r22.update()

print("Next bus is in approximately %d seconds" % r22.next_stop)

print("Route is", r22)
