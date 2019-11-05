n = int(input())
p = list(map(int,input().split()))

lr = [[[0,0] for _ in range(n)] for _ in range(n)]


for li in range(n-1):
    for ri in range(li+1,n):
        lr[li][ri][0] = p[li]


ans = 0
for li in range(n-1):
    for ri in range(li+1,n):
        if lr[li][ri][0] <= p[ri]:
            lr[li][ri][1] = lr[li][ri][0]
            lr[li][ri][0] = p[ri]

        elif lr[li][ri][1] <= p[ri]:
            lr[li][ri][1] = p[ri]

    ans += lr[li][ri][1]

for i in range(n):
    print(lr[i])

print(ans)