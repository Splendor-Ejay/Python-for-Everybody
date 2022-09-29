hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
h = float(hours)
r = float(rate)
def computepay(h, r):
    if h <= 40:
        p = h * r
    else:
        a = h * r
        b = (h-40) * (r * 0.5)
        p = a + b
    return p
h = computepay(45, 10.50)
print("Pay", h)
