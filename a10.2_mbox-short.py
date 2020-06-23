name = input("Enter file:")
try:
    handle = open(name)
    lst=list()
    counts=dict()
    for line in handle :
        if not line.startswith("From "):
            continue

        line=line.strip().split()
        hours=line[5]
        hours=hours[:2]
        lst.append(hours)

    for hour in lst :
        counts[hour]=counts.get(hour,0)+1

    for k,v in sorted(counts.items()) :
        print(k,v)
except:
    print(name, 'does not exist!!!')
