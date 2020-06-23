import xml.etree.ElementTree as ET
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

tree = ET.fromstring(data)

lst = tree.findall('.//count')
count = 0
for item in lst:
	count = count + int(item.text)

print(count)

#http://py4e-data.dr-chuck.net/comments_42.xml