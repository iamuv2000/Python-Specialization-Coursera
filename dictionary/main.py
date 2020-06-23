filename = input("Please enter filename: ")
try:
	handle = open(filename)
except:
	print("Sorry, could not find file!")
	quit()

hist = dict()
for line in handle:
	line = line.rstrip()
	words = line.split()
	for word in words:
		hist[word] = hist.get(word,0) + 1

bigcount = None
bigword = None
for key,value in hist.items():
    if(bigcount == None):
        bigcount = value
        bigword = key
    else:
        if(value > bigcount):
            bigword = key
            bigcount = value
print(bigword , bigcount)  