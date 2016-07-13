name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()[1]
        counts[words] = counts.get(words,0) + 1
              
bigcount = None
bigword = None 
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word 
		bigcount = count 
print bigword, bigcount