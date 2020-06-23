fname = input("Enter file name: ")

try:
    fh = open(fname)
    count = 0
    total = 0
    for line in fh:
        line = line.rstrip()
        if not line.startswith("X-DSPAM-Confidence:") :
            continue
        n = line.find('0')
        number = float(line[n:])
        count = count + 1
        total = total + number
    print("Average spam confidence:", total/count)
except:
    print(fname,'does not exist!!!')
