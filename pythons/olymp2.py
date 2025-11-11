A = list(map(int, input().split()))
B = list(map(int, input().split()))
N = len(A)
C = []


for i in range(N-1):
    if len(C) == N:
        break
    C.append(A[i] + B[i])
    for j in range(N-i):
        if len(C) == N:
            break
        if A[i+j] + B[i+j+1] > A[i+j+1] + B[i+j]:
            C.append(A[i+j+1] + B[i+j])
            if len(C) == N:
                break
            C.append(A[i+j] + B[i+j+1])
            continue
        C.append(A[i+j] + B[i+j+1])
        if len(C) == N:
            break
        C.append(A[i+j+1] + B[i+j])
print(C)
