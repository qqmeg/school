odd = ['1', '3', '5', '7']


def tobase(n, base):
    if n < base:
        return str(n)
    else:
        return tobase(n // base, base) + str(n % base)
    
count = 0
for n in range(8**5, 8**6):
    s = oct(n)[2:]
    if s.count('4') != 2:
        continue
    indices = [i for i, ch in enumerate(s) if ch == '4']
    if indices[1] - indices[0] == 1:
        continue
    between = s[indices[0]+1:indices[1]]
    if all(ch in '01235' for ch in between):
        without_4 = s.replace('4', '')
        if len(set(without_4)) == 4:
            count += 1
print(count)
'''
def Warning(s):
    f = s.find('4')
    f1 = s[f+1:].find('4') + len(s[:f+1])
    
    if  (f1 != -1) and (f != -1) and f1 - f > 1 and s.find('4') == -1:
        s = s[:f] + s[f1+1:]
        b = s[:s.index('4')] + s[s.index('4')+1:]
        if s.find('4') == -1 and len(b) == len(set(b)):
        # return all(int(s[f+1:f1][i]) > 5 for i in range(len(s[f+1:f1])))
            return s[f+1:f1], f, f1
    return False

#4 
c = 0
for i in range((8**4) - 10, 1000000):
    b = tobase(i, 8)
    if len(b) == 6:
        w = Warning(b)
        if w:
            print(b, w) 
        if w and all(int(w[0][i]) >= 5 for i in range(len(w[0]))):
            b = b[:w[1]] + b[w[1]+1:]
            b = b[:b.index('4')] + b[b.index('4')+1:]
            print(b, len(b), len(set(b)))
            if len(set(b)) == len(b):
                c += 1
        

print(c)
'''
exit(0)



# 3
def Warning(s):
    ind = s.index('0')
    if ind == len(s) - 1:
        if s[ind - 1] not in odd:
            return True
    if s[ind - 1] not in odd and s[ind + 1] not in odd:
        return True
    return False

c = 0
for i in range(6550, 1000000):
    b = tobase(i, 9)
    if len(b) == 5 and b.count('0') == 1 and Warning(b):
        c += 1
print(c)

exit(0)
# 6406
c = 0
for a1 in ['а', 'в', 'н', 'р', 'ь', 'я']:
    for a2 in ['а', 'в', 'н', 'р', 'ь', 'я']:
        for a3 in ['а', 'в', 'н', 'р', 'ь', 'я']:
            for a4 in ['а', 'в', 'н', 'р', 'ь', 'я']:
                for a5 in ['а', 'в', 'н', 'р', 'ь', 'я']:
                    s = a1 + a2 + a3 + a4 + a5
                    c += 1
                    if s == 'ьяряр':
                        print(c)





exit(0)




# 2

c = 0
for i in range(4090, 100000):
    b = tobase(i, 8)

    if len(b) == 5 and b[0] not in odd and b[-1] not in ['2', '6'] and b.count('7') <= 2:
        c += 1
print(c)
    






# 1
exit(0)
c = 0
for i in range(1000, 1000000):
    b = tobase(i, 9)
    if b.count('1') >= 2 and b[-1] != '2' and b[-1] != '3' and b[1] not in odd and len(b) == 6:
        c += 1
print(c)