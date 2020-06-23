fname = input("Enter file name: ")

try:
    counts = dict()
    lst = list()
    fh = open(fname)

    for line in fh:
        if not line.startswith('From:'):
            continue
        else:
            line = line.split()
            lst.append(line[1])
    for word in lst:
        counts[word] = counts.get(word,0)+1

    bigcount = None
    bigword = None
    for word,count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
    print(bigword, bigcount)
except:
    print(fname,'does not exist!!!')
