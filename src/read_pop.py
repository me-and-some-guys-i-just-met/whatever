from Classes.arrondissement import Arrondissement
from data_parsers.local_data_dir import data_dir

stops = "FIXME"
area = "FIXME"

burrows = dict()

# with open("../data/population-quartiers-anciens-territoires-administratifs.csv") as pop_file:
with open("../data/Boroughs_of_Montreal") as pop_file:
    pop_file.readline()
    for line in pop_file:
        name, popu, area = line.strip().split()
        name = name.strip()
        burrows[name] = Arrondissement(name, stops, area, popu)

for boro in burrows:
    print(boro + ": " + str(burrows.get(boro)))
