import requests

TFL_API_APP_ID = ""
TFL_API_APP_KEY = ""
MY_STOP = ""

class TFLBase:
    pass

class Stop(TFLBase):
    stop_point = None
    stop_time = None

    def show_arrivals():
        pass

class Transport(TFLBase):
    pass

class Bus(Transport):
    route = None
    stop = None
    json = None

    route_stops = []
    next_stop = None

    def __init__(self, route=None, stop=None):
        self.route = route
        self.stop = stop
        print("Created route", self.route)

    def update(self):
        req = requests.get("https://api.tfl.gov.uk/StopPoint/%s/Arrivals?app_id=%s&app_key=%s")
        self.json = req.json()
        self.next_stop = self.json[0]['timeToStation']

    def status(self):
        pass

    def __str__(self):
        return self.route

r22 = Bus(route="R22", stop=MY_STOP)

r22.update()

print("Next bus is in approximately %d seconds" % r22.next_stop)

print("Route is", r22)
