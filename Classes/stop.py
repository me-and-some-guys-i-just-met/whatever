class Stop:

    def __init__(self, stop_id = None, code = None, name = None, lat = None, lon = None, busses = None):
        self.stop_id = stop_id
        self.code = code
        self.name = name
        self.coordinates = (lat, lon)
        self.busses = busses

    #Might need to extend this class in the future
