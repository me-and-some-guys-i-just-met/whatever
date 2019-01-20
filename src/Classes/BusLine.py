#NOT USED
class BusLine(object):
'''
The BusLine class represents a STM bus line with a unique bus ID/Name
and a list of bus stop objects on its route.
'''
    def __init__(self, stop_list = [], bus_id = None):
        self.stop_list = stop_list
        self.bus_id = bus_id

    def append(self, stop_obj):
        self.stop_list.append(stop_obj)

    def set_BusID(self, newid):
        self.bus_id = newid

    #Might need to extend class in the future
