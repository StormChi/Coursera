import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter postion: '))
for i in range(count):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	num = 0
	for tag in tags:
		num += 1
		if num == position:
			url = tag.get('href', None)
			print "Retrieving:", url
## the first line is not appear. done 90%. the result is ok.