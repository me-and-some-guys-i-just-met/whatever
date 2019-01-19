from local_data_dir import data_dir

with open(data_dir + "gtfs_stm/trips.txt") as trips_file:
    print("skip first line: ", trips_file.readline())
    for line in trips_file:
        print(line)
        route_id, unused, trip_id, unused, unused, unused, unused, unused, unused = line.split(",")
        print("route_id:", route_id)
        print("trip_id:", trip_id)

