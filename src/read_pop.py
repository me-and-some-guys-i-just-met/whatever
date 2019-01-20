from Classes.arrondissement import Arrondissement
from data_parsers.local_data_dir import data_dir

stops = "FIXME"
area = "FIXME"

burrows = dict()

with open("../data/population-quartiers-anciens-territoires-administratifs.csv") as pop_file:
    for i in range(5):
        pop_file.readline()
    for line in pop_file:
        name, unused, popu = line.strip().split(',')
        name = name.strip('"')
        burrows[name] = Arrondissement(name, stops, area, popu)

for boro in burrows:
    print(boro + ": " + str(burrows.get(boro)))
