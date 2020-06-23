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


# Retrieve anchor tags
tags = soup('a')
count = 1
times = 1
while(True):
	if(times > 7):
		break
	times = times + 1
	html = urllib.request.urlopen(url , context = ctx).read()
	soup = BeautifulSoup(html,'html.parser')
	tags = soup('a')
	for tag in tags:
		count = count+1
		if(count == 19):
			print(tag.get('href', None))
			url = tag.get('href', None)
			count = 1
			break
	

#http://py4e-data.dr-chuck.net/known_by_Fikret.html