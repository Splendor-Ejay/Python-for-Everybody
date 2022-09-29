hrs = input('Enter Hours:')
rate = input('Enter rate:')
fh = float(hrs)
fr = float(rate)
if fh <= 40 :
    print ('Regular')
    pay = fh * fr
else:
    print ('Overtime')
    reg = fr * fh
    ot = (fh - 40) * (fr * 1.5)
    pay = reg + ot
print ('Pay:',pay)
