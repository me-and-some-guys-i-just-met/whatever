from local_data_dir import data_dir
import Geolocation

set_of_coord=set()
print(set_of_coord)
with open(data_dir) as stops_file:
    #print("skip first line: ", stops_file.readline())
    for line in stops_file:
        stop_id, stop_code, stop_name, stop_lat, stop_lon, unused, unused, unused, unused = line.split(",")
        ##print("stop_id:", stop_id)
        #print("stop_code:", stop_code)
        #print("stop_name:", stop_name)
        #print("coords: " + stop_lat + ", " + stop_lon)
        if (stop_lat, stop_lon) in set_of_coord:
            print("ERROR: " + stop_lat + ", " + stop_lon + " in set")
        set_of_coord.add((stop_id, stop_lat,stop_lon))
        #print(set_of_coord)
results = set()
for coords in set_of_coord:
    x = Geolocation.getAddress('AIzaSyAgg6LrGSWMB_qXc9_I4kKn6Nx3lS-eChM', [coords[1], coords[2]])
    if x:
        print(x)
        results.add(x)
