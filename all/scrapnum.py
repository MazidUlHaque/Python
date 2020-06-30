import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print (count)
print (sum)
