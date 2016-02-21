import requests
import os

TFL_API_URL = "https://api.tfl.gov.uk/"

TFL_API_APP_ID = os.environ.get('TFL_API_APP_ID')
TFL_API_APP_KEY = os.environ.get('TFL_API_APP_KEY')
BUS_STOP = os.getenv('MY_STOP', '490013767A')  # Default Charing Cross Bus Stop


class TFLBase:
    query = None
    query_id = None
    filtered = None
    filtered_id = None
    subfilter = None

    def update():
        pass
        # construct url based on api_url, type, action, and keys
# return response

    def api(self):
        url = TFL_API_URL + self.query + '/'
        if self.query_id:
            url += self.query_id + '/'
        if self.filtered:
            url += self.filtered + '/'
        if self.filtered_id:
            url += self.filtered_id + '/'
        # TODO handle param args

        try:
          r = requests.get(url)
        except:
          print("Failed to get data for URL: ", url)

        print("Returning data for url: ", url)
        # TODO store last synced data time
        return r.json()


class Stop(TFLBase):
    stop_point = None
    stop_time = None

    def __init__(self):
        print("In Stop init")
        self.query = "StopPoint"


    def arrivals(self):
        self.filtered = "Arrivals"
        self.data = self.api()


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
        print("In BusStop init")
        self.query_id = stop
        self.route = route
        super().__init__()

    def status(self):
        pass

    def next_bus(self, route = None):
        if route:
            pass
        else:
            return self.data[0]['timeToStation']

    def __str__(self):
        return self.route

# Lines/Routes

class Location(TFLBase):
    pass

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



#stop  = BusStop(stop=BUS_STOP, route="R22")
stop  = BusStop(stop=BUS_STOP)
stop.arrivals()

print("Next bus is in approximately %d seconds" % stop.next_bus())

#print("Route is", r22)
