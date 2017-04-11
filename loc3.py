import re
import json
from urllib2 import urlopen
from geopy.geocoders import Nominatim



url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

lati = data['loc']
a = data['org']
c = str(lati)

geolocator = Nominatim()
location = geolocator.reverse(c)
print(location.address)
