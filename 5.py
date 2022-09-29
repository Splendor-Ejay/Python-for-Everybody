largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        fnum = int(num)
    except:
        print('Invalid input')
    if largest is None:
        largest = fnum
    elif fnum > largest:
        largest = fnum
    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum
print('Maximum is', largest)
print('Minimum is', smallest)
