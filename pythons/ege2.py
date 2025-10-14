from re import findall, finditer


def n1(text):
    reg = r"[1-9A-D][0-9A-D]*[02468AC]"
    ints = findall(reg, text)
    return len(max(ints, key=len))


def n2(text):
    reg = r"[1-9][0-9AB]*"
    intsiter = finditer(reg, text)

    ints = filter(lambda x: int(x, base=12) % 9 == 0, ints)
    return len(max(ints, key=len))


with open("24-356.txt", 'r') as f:
    text = f.read()
    print(n2(text))
