import xml.etree.ElementTree as ET
import urllib

url = 'http://python-data.dr-chuck.net/comments_250510.xml'
url_data = urllib.urlopen(url).read()
count_total = 0

tree = ET.fromstring(url_data)
results = tree.findall('comments/comment')
print 'Results:', len(results)
for counts in results:
    print 'Name', counts.find('name').text
    print 'Score', counts.find('count').text
    counts_int = counts.find('count').text
    count_total = count_total + int(counts_int)


print count_total

#Opens a website, reads and parses the data, finds the list of names and 
#scores in comments/comment goes through the list and extracts the Name data
#with "counts.find('name').text" and score with "counts.find('count').text"
#creates a running total and then prints the total