score=input("Enter Score:")
try:
    scr = float(score)
    if scr >= 0.9 and scr <= 1.0:
        print("A")
    elif scr >= 0.8 and scr <= 0.9:
        print("B")
    elif scr >= 0.7 and scr <= 0.8:
        print("C")
    elif scr >= 0.6 and scr <= 0.7:
        print("D")
    elif scr > 0 and scr <= 0.6:
        print("F")
    else:
        print("Invalid Score!!!")
except:
    print("Invalid Score!!!")
