import requests
import os
from collections import OrderedDict

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

    data = None

    def update():
        pass
        # construct url based on api_url, type, action, and keys
# return response

    def __api__(self):
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
        self.data = r.json()


class Stop(TFLBase):
    stop_point = None
    stop_time = None

    def __init__(self):
        print("In Stop init")
        self.query = "StopPoint"

    def arrivals(self):
        self.filtered = "Arrivals"
        self.data = self.api()

    def within(self, criteria=None):
        pass

    def bbox(self, bbox=None):
        pass

    def can_reach_on_line(self, lineId=None):
        pass

    def direction_to(self, stoppoint=None):
        pass

    def disruption(self, ids=None, start_date=None, end_date=None):
        self.filtered = "Disruption"

        if ids is not None:
            self.query_id = ids

        # TODO filter by date

        self.__api__()

        return self.data

    def fareTo(self, stop_point=None):
        self.filtered = "FareTo"
        self.filtered_id = stop_point

        self.__api__()

        return self.data

    def meta(self):
        pass

    def mode(self):
        pass

    def routes(self, serviceTypes="Regular"):
        self.filtered = "Route"

        self.__api__()

        # TODO Turn map line locations into something useful

        return self.data

    def query(self):
        pass

    def service_types(self):
        pass

    def type(self):
        pass


class Transport(TFLBase):
    pass

# Modes of Transport


class Bus(Transport):
    data = None

    vehicleId = None
    lineName = None
    destinationName = None
    currentLocation = None
    direction = None
    expectedArrival = None
    timeToStation = None

    def __init__(self):
        pass

    def __data__(self, data):
        self.data = data

    def lineName(self):
        return self.data['lineName']

    def timeToStation(self):
        return self.data['timeToStation']


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
    stop_routes = {}
    stop_vehicles = {}

    queue = []

    next_bus = None
    next_buses = {}

    stop = None
    json = None

    route_stops = []
    next_stop = None

    def __init__(self, stop=None, route=None):
        print("In BusStop init")
        self.query_id = stop
        self.route = route
        super().__init__()

    def __arrivals(self):
        self.filtered = "Arrivals"

        super().__api__()

        for bus in self.data:
            self.stop_routes[bus['lineName']] = 1
            self.stop_vehicles[bus['vehicleId']] = 1

        self.queue = sorted(self.data, key=lambda b: int(b['timeToStation']))

    def status(self):
        pass

    def next_bus_time(self, route=None):
        if self.data is None:
            self.__arrivals()

        if route:
            for bus in self.queue:
                if bus['lineName'] == route:
                    return bus['timeToStation']
        else:
            if self.queue is not None:
                return self.queue[0]['timeToStation']

        return None

    def next_bus(self, route=None):
        nextbus = None

        if self.data is None:
            self.__arrivals()

        if route:
            for bus in self.queue:
                if bus['lineName'] == route:
                    nextbus = Bus()
                    nextbus.__data__(bus)
        else:
            if self.queue is not None:
                nextbus = Bus()
                nextbus.__data__(self.queue[0])

        return nextbus

    def route(self):
        super().route()

    def __str__(self):
        return self.query_id

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


# stop  = BusStop(stop=BUS_STOP, route="R22")
stop = BusStop(stop=BUS_STOP)
# stop.arrivals()

print("Next bus arrives in approximately %d seconds" % stop.next_bus_time())

print("Stop is served by routes: %s" % stop.routes())

bus = stop.next_bus()

print("Next bus is on route %s" % bus.lineName())

# print("Route is", r22)
