N = int(input())
XY = sorted([list(map(int,input().split())) for _ in range(N)])

PQ = []
# 2点を選びp,q仮決め
for i in range(N):
    prev = XY[i]
    for j in range(N):
        if i!=j:
            next = XY[j]
            p = next[0] - prev[0]
            q = next[1] - prev[1]
            PQ.append((p,q))

ans = 1
for pq in PQ:
    ans = max(ans, PQ.count(pq))
print(N - ans if N>1 else 1)