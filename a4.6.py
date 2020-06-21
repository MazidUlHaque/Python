def computepay(h,r):
    con = 40
    if h <=con:
        print(h*r)
    elif h > con:
        incr = (h-con)*1.5 * r
        val = con * r
        p = val + incr

    return p

hours = input('Enter Hours:')
h = float(hours)
rate = input('Enter Rate:')
r = float(rate)

p = computepay(h,r)
print("Pay",p)
