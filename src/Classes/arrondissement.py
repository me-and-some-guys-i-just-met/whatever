class Arrondissement:
    """
Represents a Borough
    """
    def __init__(self, name, stops, area, population):
        self.name = name
        self.stops = stops
        self.area = float(area)
        self.population = int(population)

    def __repr__(self):
        return self.name + " has population " + str(self.population) + " and area " + str(self.area) + "km^-2"

    def density(self):
        return int(self.population / self.area)

    def ratio(self):
        return self.stops / (self.population * self.area)
