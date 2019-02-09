import urllib
import re
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Lael.html'
iteration = 0
#opens a new page parses it finds the 18th link and opens that 7 times
while iteration < 7:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags  = soup('a')
    url = tags[17].get('href',None)
    print "Retrieving:", url
    iteration = iteration + 1