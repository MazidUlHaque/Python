fname = input("Enter file name: ")
try:
    fh = open(fname)
    lst = list()
    for line in fh:
        words = line.rstrip().split()
        for word in words:
            if word in lst:
                continue
            lst.append(word)
    lst.sort()
    print (lst)
except:
    print(fname, 'does not exist!!!')
