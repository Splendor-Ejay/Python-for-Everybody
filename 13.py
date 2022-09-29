import re
file = open('regex_sum_1450865.txt')
total = 0
for line in file:
    line = line.rstrip()
    number = re.findall('[0-9]+', line)
#lne = [int(x) for x in number]
    for num in number:
        total = total + int(num)
print (total)
