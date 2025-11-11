from itertools import product


def tobase(n, base):
    if n < base:
        return str(n)
    else:
        return tobase(n // base, base) + str(n % base)


for k in range(20):
    cou = 0
    for x in product('01', repeat=20):
        if x.count('0') == k:
            cou += 1

    print(k, cou)


exit(0)

l = ["а", 'е', 'и', 'к', 'м', 'с', 'ч']
Warning = False
cou = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    if (s := (a + b + c + d + e)) == 'масик':
                        Warning = True
                    elif Warning == True:
                        if s == 'чечик':
                            print(cou)
                            exit(0)
                        cou += 1

exit(0)


cou = 0
for i in range(6**5, 6**6):
    i6 = tobase(i, 6)
    if i6.count('2') == 1:
        ind2 = i6.index("2")
        if ind2 not in [len(i6) - 1, 0]:
            if all([int(c) % 2 == 0 for c in [i6[ind2 - 1], i6[ind2 + 1]]]):
                cou += 1
        else:
            if ind2 == 0:
                if int(i6[ind2 + 1]) % 2 == 0:
                    cou += 1
            else:
                if int(i6[ind2 - 1]) % 2 == 0:
                    cou += 1
print(cou)

exit(0)

l = ['а', 'г', 'и', 'л', 'м', 'о', 'р', 'т']
i = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    i += 1

                    if i % 2 == 0 and (a not in ['а', 'г']) and (w := (a + b + c + d + e)).count('р') >= 2:
                        print(i)
                        exit(0)
