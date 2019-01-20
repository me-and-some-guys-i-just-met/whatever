#NOT USED
from local_data_dir import data_dir

with open(data_dir + "gtfs_stm/stop_times.txt") as stop_times_file:
    print("skip first line: ", stop_times_file.readline())
    for line in stop_times_file:
        trip_id, unused, unused, stop_id, unused = line.split(",")
        print("trip_id:", trip_id)
        print("stop_id:", stop_id)
