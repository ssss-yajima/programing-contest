N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
BC = [list(map(int,input().split())) for _ in range(M)]
BC = sorted(BC, key=lambda x:x[1], reverse=True)
D = [0] * N
idx = 0
for b,c in BC:
    for i in range(b):
        D[idx] = c
        idx += 1
        if idx >= N:
            break
    if idx >= N:
        break
# print(D)


# print(D)
# print(sorted(A))
# print(len(D), len(A))
for i in range(N):
    if A[i] < D[i]:
        A[i] = D[i]
    else:
        break
print(sum(A))