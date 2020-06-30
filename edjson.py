import json
import urllib.request,urllib.parse,urllib.error

url=input("Enter: ")
data=urllib.request.urlopen(url).read().decode()
item=json.loads(data)
print("Count: ",len(item))

sum=0
for i in range(0,len(item["comments"])):
    sum=sum+int(item["comments"][i]["count"])
print(sum)
