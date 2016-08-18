import urllib
import xml.etree.ElementTree as ET

url  = raw_input('Enter url: ')
uh = urllib.urlopen(url)
data = uh.read()
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
print 'count:', len(lst)
total = 0
for item in lst:
    total += int(item.find('count').text)
print 'sum: ', total

