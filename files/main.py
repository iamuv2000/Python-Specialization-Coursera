file_name = input("Please enter filename to open file: ")
try:
	xfile = open(file_name)
except:
	print("Sorry unable to open file: " , file_name)
	quit()
	
for hello in xfile:
	print(hello.rstrip())
#print("Line count: " , count)