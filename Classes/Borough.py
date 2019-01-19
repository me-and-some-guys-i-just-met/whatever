class Borough(object):
    '''
    This class represents a city Borough. It has a list of bus stops,
    an area and population.
    '''
    def __init__(self, busses = None):
        self.bus_stops = busses
        self.area = 0
        self.population = 0
