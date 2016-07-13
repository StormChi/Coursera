name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()[5].split(":")[0].split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
           
lst = list()
for key, val in counts.items():
	lst.append((key, val))

lst.sort()

for key, val in lst:
	print key, val