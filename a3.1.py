hours = input('Enter Hours:')
h = float(hours)
rate = input('Enter Rate:')
r = float(rate)
con = 40

if h <=con:
    print(h*r)
elif h > con:
    incr = (h-con)*1.5 * r
    val = con * r
    fval = val + incr
    print(fval)
