from local_data_dir import data_dir

with open(data_dir + "gtfs_stm/stops.txt") as stops_file:
    print("skip first line: ", stops_file.readline())
    for line in stops_file:
        stop_id, stop_code, stop_name, unused, unused, unused, unused, unused, unused = line.split(",")
        print("stop_id:", stop_id)
        print("stop_code:", stop_code)
        print("stop_name:", stop_name)
