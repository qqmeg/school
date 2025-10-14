
def divisors(n: int) -> list:
    divs = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(int(n/i))
    return divs



def factork(n, k): # протое разложение на k множителей если не получается, то []
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and (len(list(divisors(i))) == 0):
            while n % i == 0:
                n//= i
                factors.append(i)
                if (len(factors) == k and n == 1) or (len(list(divisors(n))) == 0 and n != 1 and len(factors) == k - 1):
                    if n != 1:
                        factors.append(n)
                    return factors
    return []


yi =  6086055 + 1

l = []
while len(l) < 5:
    div = list(divisors(yi))
    factor2 = factork(yi, 2)
    if factor2:
        if str(factor2[0]).count('6') == str(factor2[1]).count('6') == 1:
            l.append((yi, max(factor2)))
    yi += 1
            
for i in l:
    print(*i)
# 23569
exit(0)

yi = 7305678 + 1
l = []

while len(l) < 5:
    factors4 = factork(yi, 4)
    if factors4:
        if sum(factors4) and str(sum(factors4)) == str(sum(factors4))[::-1]:
            l.append((yi, sum(factors4)))
    yi += 1

for i in l:
    print(*i)

exit(0)



# 17879
yi = 800000 + 1
l = []


while len(l) < 5:
    div = list(divisors(yi))
    if div and str(M:=(min(div) + max(div)))[-1] == '4':
        l.append((yi, M))
    yi += 1

for i in l:
    print(*i)

exit(0)



# 1256
def factors(n: int) -> list:
    cou2 = 0
    cou3 = 0
    while n % 4 == 0:
        n //= 4
        cou2 += 2
    while n % 3 == 0:
        n //= 3
        cou3 += 1

    return True if (cou3 % 2 != 0 and n == 1) else False



for i in range(200000004, 400000000, 6):
    if factors(i):
        print(i)
        





exit(0)

# 21422
yi = 1125000 + 1

l = []

while len(l) < 5:
    div = list(divisors(yi))
    f = list(filter(lambda x: str(x)[-1] == '7' and x != 7, div))
    if f:
        l.append((yi, min(f)))
    yi += 1

for i in l:
    print(*i)





exit(0)

# 21909

yi = 500000 + 1

l = []

while len(l) < 5:
    div = list(divisors(yi))
    div.extend([1, yi])
    R = sum(div)
    if str(R)[-1] == '6':
        l.append((yi, R))
    yi += 1

for i in l:
    print(*i)





exit(0)
# 1206
'''
Напишите программу, которая ищет среди целых чисел, превышающих 350300, 
первые шесть чисел, удовлетворяющих условию: сумма всех различных делителей числа, отличных от 1 и самого числа, кратна 13.

В ответе запишите эти шесть пар чисел в порядке возрастания первого числа в паре:
 число, для каждого такого числа частное от деления на 13 суммы его различных делителей (исключая 1 и само число).
'''

yi = 350301
l = []
while len(l) < 6:
    div = list(divisors(yi))

    if sum(div) % 13 == 0:
        l.append((yi, sum(div)//13))
    yi += 1
for i in l:
    print(*i)


exit(0)
'''
Напишите программу, которая ищет среди целых чисел, 
превышающих 136179, первые четыре числа, удовлетворяющих условию: сумма всех различных 
делителей числа, отличных от 1 и самого числа, при делении на 385 даёт остаток 91.

В ответе запишите эти четыре пары чисел в порядке возрастания первого числа в паре: 
число и сумму его различных делителей (исключая 1 и само число).
'''
# 1274
yi = 136180
l = []
while len(l) < 4:
    div = list(divisors(yi))

    if sum(div) % 385 == 91:
        l.append((yi, sum(div)))
    yi += 1

for i in l:
    print(*i)

exit(0)
# 1303
l = []
yi = 452022
while len(l) < 5:
    div = list(divisors(yi))
    
    M = max(div) + min(div) if div else 0
    if M % 7 == 3:
        l.append((yi, M))
    yi += 1

for i in l:
    print(*i)


