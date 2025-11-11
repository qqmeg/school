res = 0
with open("csv/ege231.csv", "r", encoding="utf-8") as file:
    data = file.readlines()
    print(data)
    for line in data:
        c = line.strip().split(",")
        if c[-1] == "Поступление":
            res += int(c[-2])

print(res)
a = 1
