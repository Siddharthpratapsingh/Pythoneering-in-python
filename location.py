import urllib2
from lxml import etree
import pyttsx
import requests


# List to store all article-urls from each page
engine = pyttsx.init()

#Now request is being send to each article page and required data is scraped        
page = "https://www.mapdevelopers.com/what-is-my-address.php"
hdr = {'User-Agent': 'Chromium_Browser'}
req = urllib2.Request(page,headers=hdr)
response = urllib2.urlopen(req)
htmlparser = etree.HTMLParser()
tree = etree.parse(response,htmlparser)
title = tree.xpath('//div[@class="col-xs-3 col-sm-4 col-md-4"]/text()')
engine.say(title)
print(title)

engine.runAndWait()   



