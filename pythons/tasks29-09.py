from collections import Counter



with open('9_18258.csv') as f: 
    file = f.read().strip().split('\n')
    listlines = list(map(lambda x: list(map(int, x.split(','))), file))

    for i in listlines:
        from collections import Counter
        c = dict(Counter(i))
        for i in c.keys():
            if c[i] < 2:
                c.pop(i)
        povt = [i for i in c.keys() if c[i] >= 2]
        if sorted(i, reverse=True) == i and any(povt, key=lambda x: x):
            pass





exit(0)
#18943
cou = 0
with open('9_18943.csv') as f:
    file = f.read().strip().split('\n')
    listlines = list(map(lambda x: list(map(int, x.split(','))), file))

    for i in listlines:
        c = Counter(i)
        tri = [num for num, count in c.items() if count == 3]
        two = [num for num, count in c.items() if count == 2]
        dif = set(i).difference(set(tri))
        dif = set(dif).difference(set(two))
        if len(dif) == 2 and sum(tri) + sum(two) >= sum(dif):
            cou += 1

print(cou)








exit(0)

def divisors(n: int) -> list:
    divs = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(int(n/i))
    # divs.add(n) 224
    return divs





def iscube(n):
    x = round(n ** (1/3))
    return x**3 == n and n % 2 != 0


for i in range(326496, 649632):
    div = list(divisors(i))
    if (a1:=len(list(filter(lambda x: x % 2 != 0, div)))) == (a2:=len(list(filter(lambda x: x % 2 == 0, div)))) and a1 >= 70 and a2 >= 70:
        minmore1000 = min(filter(lambda x: x > 1000, div))
        print(i, minmore1000)

exit(0)
# 224
for i in range(228224, 531136):
    if len(l:=list(filter(iscube, list(divisors(i))))) >= 4:
        
        print(len(l), max(l))



exit(0)
# 280
for i in range(333555, 778000):
    if len(t:=list(filter(lambda x: len(x) == 2, map(str, list(divisors(i)))))) == 35:
        print(int(min(t)), int(max(t)))



'''
for i in range(135790, 163229):
    if sum(a:=divisors(i)) > 460000:
        print(len(a), sum(a))
'''
exit(0)


cou = 0
for i in range(81234, 134690): # n, k
    if len(divisors(i)) == 3: # == 2
        cou += 1
        print(*sorted(list(divisors(i))))
        





        
exit(0)

with open('9_23747.csv') as f:
    max_index = -1
    max_sum = None
    for idx, line in enumerate(f):
        nums = list(map(int, line.strip().split(',')))
        if len(nums) != 7:
            continue
        from collections import Counter
        c = Counter(nums)
        # Найти число, встречающееся трижды
        triplet = [num for num, count in c.items() if count == 3]
        # Проверить, что ровно одно такое число и остальные уникальны
        if len(triplet) == 1 and len([num for num, count in c.items() if count == 1]) == 4:
            uniq = [num for num, count in c.items() if count == 1]
            avg_uniq = sum(uniq) / 4
            if avg_uniq <= triplet[0]:
                max_index = idx
                max_sum = sum(nums)
    print(max_sum)
exit(0)


cou = 0
with open('15-09/9-227.csv') as f:
    for x in f:
        x = sorted(map(int, x.strip().split(",")), reverse=True)
        if len(set(x)) == 3 and (x[0] + x[1] > 2*(x[2] + x[3])) and (x[0] % x[-1] != 0):
            cou += 1
print(cou)


exit(0)

1
cou = 0
with open('15-09/9-164.csv') as f:
    for x in f:
        x = sorted(map(int, x.strip().split(",")), reverse=True)
        if (x[-1]**2)*2 > x[1]*x[2] and len(set(x)) <= 3:
            cou += 1

print(cou)




cou = 0
with open('15-09/9-160.csv') as f:
    for x in f:
        x = sorted(map(int, x.strip().split(",")), reverse=True)
        if (x[0] < sum(x) - x[0]) and x[0] + x[3] == x[1] + x[2]:
            cou += 1
print(cou)
            





cou = 0
with open('15-09/9-161.csv') as f:
    for x in f:
        x = sorted(map(int, x.strip().split(",")), reverse=True)
        if x[0] < (x[1] + x[2] + x[3]) and len(set(x)) == 3:
            cou += 1
print(cou)



