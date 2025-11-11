
n = int(input())
res = []
for _ in range(n):
    a = int(input())
    if str(360/(180-a)).split('.')[-1] == '0' and 360//(180-a) >= 3:
        res.append("YES")
    else:
        res.append("NO")
print("\n".join(res))
        