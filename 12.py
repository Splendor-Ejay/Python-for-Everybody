name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
time = dict()
for line in handle :
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1:
        continue
    if wds[0] != 'From' :
        continue
    wds = line.split()
    hour = wds[5]
    hour = hour.split(':')
    hr = hour[0]
    #print(hr)
    time[hr] = time.get(hr,0) + 1

x = sorted(time.items())
for k,v in x:
    print (k,v)
