import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certidfication errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url  = input("Enter- ")
html = urllib.request.urlopen(url , context = ctx).read()
soup = BeautifulSoup(html,'html.parser')

total = 0

# Retrieve anchor tags
tags = soup('span')
for tag in tags:
	total = total + int(tag.contents[0])

print(total)

#http://py4e-data.dr-chuck.net/comments_42.html