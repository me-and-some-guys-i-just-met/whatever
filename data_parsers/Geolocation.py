import requests
#from api_key import key

#Reverse GeoCoding
#required parameters:
#latlng - the lat and long
#key - the API key

#Optional street_type: street_address | route | intersection | locality

url = r'https://maps.googleapis.com/maps/api/geocode/json?'

def getAddress(key, latlng):
    global url
    req = url + 'latlng=' + latlng[0] + ',' + latlng[1] + '&key=' + key
    response = requests.get(req)
    if response.status_code == '200':
        #parse the content which is in json format
        pass
