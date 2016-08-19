import urllib
import json

url = raw_input("Enter url: ")
uh = urllib.urlopen(url)
data = uh.read()

info = json.loads(data)
total = 0
for item in info["comments"]:
    total += item["count"]
print "Sum:", total 
