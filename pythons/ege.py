'''
import re
with open("24-235.txt", 'r') as f:
    file = str(f.read())
    reg = r"X\wP"
    l = re.findall(reg, file)
    d = {}
    st = "XYZOWP"
    for e in st:
        d[e] = 0
    for i in l:
        d[i[1]] += 1
    print(max(d.values()))
''


import re

from itertools import accumulate

print(list(accumulate(filter(lambda x: x % 2, [int(i) for i in str(
    max([int(i[2:-2]) for i in re.findall(r"ZZ8\d\d\d54\d\d\d22ZZ", str(open("24-230.txt", 'r').read()))]))]), lambda
    x, y: x*y))[-1])

'''


import re


with open("24-280.txt", 'r') as f:
    file = str(f.read()).split("A")
    reg = r"(?=([^Y]*X[^X]*Y[^XY]*))"
    reg2 = r"(?=([^X]*Y[^Y]*X[^XY]*))"
    maxass = ''
    for i in file:
        ass = max(re.findall(reg, i))
        ass2 = max(re.findall(reg2, i))
        maxass12 = max(ass, ass2) if len(ass + ass2) != 0 else ''
        maxass = maxass if len(maxass) > maxass12 else maxass12
    print(maxass)
