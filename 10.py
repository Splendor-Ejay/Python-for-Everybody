fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1:
        continue
    if wds[0] != 'From' :
        continue
    count = count + 1
    print(wds[1])
print("There were", count, "lines in the file with From as the first word")
