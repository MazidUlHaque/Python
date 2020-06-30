import re

fname = open("regex_sum_679905.txt")
lst=list()
for line in fname:
     search = re.findall('[0-9]+',line)
     lst = lst+search

sum=0
for val in lst:
    sum = sum + int(val)

print(sum)
