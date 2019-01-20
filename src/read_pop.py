from Classes.arrondissement import Arrondissement
from data_parsers.local_data_dir import data_dir

burrows=dict()
burrows_object=dict()
with open("Classes/population-quartiers-anciens-territoires-administratifs.csv") as pop_file:
  for i in range(5):
    pop_file.readline()
  for line in pop_file:
      #print(line.split(','))
      name, unused, popu = line.strip().split(',')
      name=name.strip('"')
      burrows[name]=popu


for i in burrows:
    burrows_object[i]=Arrondissement(i,0,0,burrows.get(i))
    print(burrows_object.get(i))

##print(burrows_object)
