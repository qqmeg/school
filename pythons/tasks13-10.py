l = [(int(str(k)[:-2])*113, k) for k in range(100, 10000000)]
print(list(filter(lambda x: x[0] == x[1], l)))