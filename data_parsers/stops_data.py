from local_data_dir import data_dir

set_of_coord=set()
print(set_of_coord)
with open(data_dir + "gtfs_stm/stops.txt") as stops_file:
    #print("skip first line: ", stops_file.readline())
    for line in stops_file:
        stop_id, stop_code, stop_name, stop_lat, stop_lon, unused, unused, unused, unused = line.split(",")
        ##print("stop_id:", stop_id)
        #print("stop_code:", stop_code)
        #print("stop_name:", stop_name)
        #print("coords: " + stop_lat + ", " + stop_lon)
        set_of_coord.add((stop_lat,stop_lon))
        #print(set_of_coord)
    
print(len(set_of_coord))

