text = "X-DSPAM-Confidence:    0.8475";
begin = text.find('0')
num = text[begin:]
number = float(num)
print(number)
