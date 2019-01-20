import requests
import json
#from api_key import key

#Reverse GeoCoding
#required parameters:
#latlng - the lat and long
#key - the API key

#Optional street_type: street_address | route | intersection | locality



url = r'https://maps.googleapis.com/maps/api/geocode/json?'
# url = r'https://danso.ca/aoueahtns/json?'

def getAddress(key, lat, lon):
    '''
    Using google's Geolocation API, we can get the street address +
    Borough that the coordinates point to.
    '''
    req = url + 'latlng=' + lat + ',' + lon + '&location_type=ROOFTOP&result_type=street_address'+'&key=' + key
    response = requests.get(req)
    boro = None
    if response.status_code == 200:
        loc_json = json.loads(response.content)
        try:
            boro = loc_json['results'][0]['address_components'][2]['long_name']
        except Exception as e: # malformed JSON
            print("error: parsing: " + str(e))
    else: # not 200
        print("error: HTTP " + str(response.status_code))
    return boro
