fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    uline = line.rstrip()
    print(uline.upper())
