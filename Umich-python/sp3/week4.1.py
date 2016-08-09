import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
total = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    count = count + 1
    total += int(tag.contents[0])
    
print 'Count',count
print 'Sum', total 