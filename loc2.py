import re
import json
from urllib2 import urlopen

url = 'http://ip-api.com/json'
response = urlopen(url)
data = json.load(response)

latitude = data['lat']
longitude = data['lon']
a = data['as']
print latitude
print longitude
print a



