fname = input("Enter file name: ")
try:
    fh = open(fname)
    for line in fh:
        line = line.rstrip().upper()
        print(line)
except:
    print(fname, 'file does not exist!!')
