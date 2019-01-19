class Arrondissement:

    def __init__(self, name, stops, size, population):
        self.name = name
        self.stops = stops
        self.size = size
        self.population = population

    def density(self):
        return population / size
