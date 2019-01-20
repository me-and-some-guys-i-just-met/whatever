class Arrondissement:
'''
Represents a Borough
'''
    def __init__(self, name, stops, area, population):
        self.name = name
        self.stops = stops
        self.area = area
        self.population = population

    def __repr__(self):
        return self.name + " has population " + str(self.population) + " and area " + str(self.area) + "km^-2"

    def nice_string(self):
        return self.name + "\t" + self. area + "\t" + self.population

    def density(self):
        return population / area
