class Arrondissement:

    def __init__(self, name, stops, area, population):
        self.name = name
        self.stops = stops
        self.area = area
        self.population = population

    def __repr__(self):
        return self.name + " has population " + str(self.population)

    def density(self):
        return population / area
