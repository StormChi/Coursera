import re
txt = open("/Users/storm/Downloads/regex_sum_200507.txt")
total = 0
for line in txt:
	num = re.findall('[0-9]+', line)
	if num != []:
		for i in num:
			total += int(i)
print total