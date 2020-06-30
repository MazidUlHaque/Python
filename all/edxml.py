import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter location: ")
if len(url) < 1:
    url = " http://py4e-data.dr-chuck.net/comments_679909.xml"
print ("Retrieving " + url)

xml  = urllib.request.urlopen(url, context=ctx).read()
print ("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print ("Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print ("Sum:" + str(accumulator))
