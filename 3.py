scr = input('Enter Score: ')
score = float(scr)
try:
    if score > 1.0:
        print ('Grade must be beween 0 and 1')
    if score >= 0.9:
        print ('A')
    elif score >= 0.8:
        print ('B')
    elif score >= 0.7:
        print ('C')
    elif score >= 0.6:
        print ('D')
    else:
        print ('F')
except:
    print ('Grade must be beween 0 and 1')
