#import url, regular expressions, beautiful soup
import urllib
import re
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_250513.html"

#open the url, parse it, look for span tags
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = 0
tags  = soup("span")

#go through the tags
for tag in tags:
    for words in tag: #look through the words in the tag
        y = re.findall("[0-9]+", words) #find the number which is a string
        y = [int(soup_list) for soup_list in y] #convert the string into a int 
        count = count + sum(y) #int is in a list so sum the list and add to count
print count