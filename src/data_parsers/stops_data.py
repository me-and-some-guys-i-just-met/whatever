from local_data_dir import data_dir
import Geolocation
from stop import Stop

#The script that does all the heavy lifting. Take the data sets, sends a request
#to the google maps API and outputs to a file

stops = set()
print(stops)

with open(data_dir + "gtfs_stm/stops.txt") as stops_file:
    for line in stops_file:
        stop_id, stop_code, stop_name, stop_lat, stop_lon, unused, unused, unused, unused = line.split(",")
        stops.add(Stop(stop_id, stop_lat, stop_lon))

print("done preparing")

success_count = 0
fail_count = 0

with open("../../Borough_Results.txt", mode="a") as output_file:
    try:
        for stop in stops:
            boro = Geolocation.getAddress('AIzaSyAgg6LrGSWMB_qXc9_I4kKn6Nx3lS-eChM', stop.lat, stop.lon)
            if boro is not None:
                output_file.write(f"{stop.stop_id}, {stop.lat}, {stop.lon}, {boro}\n")
                output_file.flush()
                print(f"{stop.stop_id} , {stop.lat} , {stop.lon} , {boro}")
                success_count += 1
            else:
                fail_count += 1
    except KeyboardInterrupt:
        pass

print("successes: " + str(success_count));
print("failures: " + str(fail_count));
