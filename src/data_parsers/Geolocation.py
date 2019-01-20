import requests
import json
#from api_key import key

#Reverse GeoCoding
#required parameters:
#latlng - the lat and long
#key - the API key

#Optional street_type: street_address | route | intersection | locality

url = r'https://maps.googleapis.com/maps/api/geocode/json?'

def getAddress(key, latlng):
    global url
    req = url + 'latlng=' + latlng[0] + ',' + latlng[1] + '&location_type=ROOFTOP&result_type=street_address'+'&key=' + key
    response = requests.get(req)
    if response.status_code == 200:
        loc_json = json.loads(response.content)
        final_address = [loc_json['results'][0]['address_components'][0]['long_name'], loc_json['results'][0]['address_components'][1]['long_name'], loc_json['results'][0]['address_components'][2]['long_name']]
        print(final_address)
    else:
        print(type(response.status_code))
    return
