#NOT USED
from local_data_dir import data_dir

with open(data_dir + "gtfs_stm/routes.txt") as routes_file:
    print("skip first line: ", routes_file.readline())
    for line in routes_file:
        route_id, unused, route_short_name, route_long_name, unused, unused, unused, unused = line.split(",")
        print("route_id:", route_id)
        print("route_long_name:", route_long_name)
        print("route_short_name:", route_short_name)
