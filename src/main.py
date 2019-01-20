from data_parsers import read_stops, read_pop, link_data

#Take the bus stops dataset and build a simplified dataset with the stop ids
#the lattitude and longitude and the borough it belongs to


print("Welcome to our hackatown project. \nTo use this program, you need a dataset with"+
"the lattitude and longitude of bus stops in your city, \na dataset with population data of each borough"+
"a valid API key for the google maps API")

#parser = parser.ArgumentParser(description="This script is used to examine the population density vs the bus stop density")

#parser.add_argument("path", action = 'store', type = str, help="")

bus_stops_path = str(input("Input the path to the bus stops dataset:"))
boroughs_path = str(input("Input the path to the boroughs dataset:"))
API_key = str(input("Input the google maps API key"))

print("Starting the process")

print("Starting with the stops dataset")
Stops_Parser(bus_stops_path, API_key)
print("Done")

print("Starting with the boroughs dataset")
format_popfile(boroughs_path)
print("Done")

print("Creating ratings dataset")
end_results()
print("All Done")
