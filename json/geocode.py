import json
import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore SSL Certidfication errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url  = "http://py4e-data.dr-chuck.net/json?"
key=42
address = input("Address- ")

params = dict()
params["address"] = address
params["key"] = key


url = url + urllib.parse.urlencode(params)


handle = urllib.request.urlopen(url , context = ctx)

data = handle.read()
data.decode()

data = json.loads(data)

print(data["results"][0]["place_id"])

#South Federal University