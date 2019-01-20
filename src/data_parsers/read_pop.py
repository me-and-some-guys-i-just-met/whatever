#NOT USED
from Classes.arrondissement import Arrondissement

#stops = "FIXME"
#area = "FIXME"


def format_popfile(path):
    burrows = dict()

    #opens dataset for the population statistics of all the boroughs of Boroughs_of_Montreal
    #and creates a class
    with open(path, 'r') as pop_file:
        pop_file.readline()
        for line in pop_file:
            name, popu, area = line.strip().split()
            name = name.strip()
            burrows[name] = Arrondissement(name, stops, area, popu)

    with open('../data/formatted_boroughs.txt', 'w') as f_b:
        for boro in burrows:
            f_b.write(boro.nice_string)
