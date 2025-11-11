from itertools import product


def tobase(n, base):
    digits = "0123456789ABCDEF"
    s = ""
    while n:
        s = digits[n % base] + s
        n //= base
    return s if s else "0"


if True:
    count = 0
    for a in "1234567":
        for rest in product("01234567", repeat=6):
            b, c, d, e, f, g = rest
            s8 = a + b + c + d + "2" + e + f + g + "3"
            x = int(s8, 8)
            if (x // 256) % 16 == 10:
                count += 1
    print(count)
    exit(0)


if False:
    last_valid_index = 0
    for n in range(10000, 100000):
        index = n - 10000 + 1
        s = str(n)
        valid = True
        for i in range(len(s) - 1):
            if (int(s[i]) % 2 == 0 and int(s[i + 1]) % 2 == 0) or (
                int(s[i]) % 2 == 1 and int(s[i + 1]) % 2 == 1
            ):
                valid = False
                break
        if valid and index % 15 == 0:
            last_valid_index = index
    print(last_valid_index)
    exit(0)


if False:
    count = 0
    for n in range(12**4, 12**5):
        s = tobase(n, 12)
        cnt_pairs = 0
        for i in range(len(s) - 1):
            d1 = int(s[i], 12)
            d2 = int(s[i + 1], 12)
            if d1 % 2 == 1 and d2 % 2 == 1:
                cnt_pairs += 1
        if cnt_pairs <= 2:
            count += 1
    print(count)
    exit(0)


if False:
    count = 0
    for n in range(7**4, 7**5):
        s = tobase(n, 7)
        cnt_pairs = 0
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == 0 and int(s[i + 1]) % 2 == 0:
                cnt_pairs += 1
        if cnt_pairs >= 2:
            valid = True
            for i in range(len(s) - 2):
                if (
                    int(s[i]) % 2 == 0
                    and int(s[i + 1]) % 2 == 0
                    and int(s[i + 2]) % 2 == 0
                ):
                    valid = False
                    break
            if valid:
                count += 1
    print(count)
    exit(0)


if False:
    count = 0
    for n in range(5**8, 5**9):
        s = tobase(n, 5)
        cnt_pairs = 0
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == 0 and int(s[i + 1]) % 2 == 0:
                cnt_pairs += 1
        if cnt_pairs == 2:
            valid = True
            for i in range(len(s) - 2):
                if (
                    int(s[i]) % 2 == 0
                    and int(s[i + 1]) % 2 == 0
                    and int(s[i + 2]) % 2 == 0
                ):
                    valid = False
                    break
            if valid:
                count += 1
    print(count)
    exit(0)


if False:
    from itertools import product

    alphabet = "АКОРСТ"
    count_index = 0
    last_even = 0
    for word in product(alphabet, repeat=5):
        count_index += 1
        if word[0] in "АСТ":
            continue
        if word.count("О") != 2:
            continue
        if count_index % 2 == 0:
            last_even = count_index
    print(last_even)
    exit(0)
