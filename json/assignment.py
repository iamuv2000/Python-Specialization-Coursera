import json
import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore SSL Certidfication errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url  = input("Enter- ")
handle = urllib.request.urlopen(url , context = ctx)

data = handle.read()
data.decode()

data = json.loads(data)

count = 0


for comment in data["comments"]:
	count = count + int(comment["count"])

print(count)


#http://py4e-data.dr-chuck.net/comments_42.json