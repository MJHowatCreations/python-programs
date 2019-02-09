import json
import urllib

assignment_url = 'http://python-data.dr-chuck.net/comments_250514.json'
uh = urllib.urlopen(assignment_url)
data = uh.read()
info = json.loads(data)
running_total = 0

for items in info["comments"]:
        print 'Name', items["name"]
        print 'Count', items["count"]
        running_total = running_total + items["count"]

print 'Total', running_total