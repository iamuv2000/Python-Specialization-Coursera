import re
handle = open('text.txt')

numbers = (re.findall('[0-9]+',handle.read().strip()))

total = 0

for number in numbers:
	total = total + int(number)

print(total)