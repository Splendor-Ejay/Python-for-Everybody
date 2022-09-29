name = input('Enter file: ')
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mails = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1:
        continue
    if wds[0] != 'From' :
        continue
    wds = line.split()
    mails[wds[1]] = mails.get(wds[1],0) + 1

largest = -1
largestauthor = None
for k,v in mails.items() :
    if v > largest :
        largest = v
        largestauthor = k

print(largestauthor,largest)
