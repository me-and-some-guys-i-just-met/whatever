class Stop:

    def __init__(self, stop_id = None, stop_code = None, stop_name = None, lat = None, long = None, busses = None):
        self.stop_id = stop_id
        self.stop_code = stop_code
        self.stop_name = stop_name
        self.coordinates = [lat, long]
        self.busses = busses

    #Might need to extend this class in the future