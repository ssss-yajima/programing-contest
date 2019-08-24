n,m,c = map(int,input().split())
bb = list(map(int, input().split()))
aa = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for a in aa:
    total = c
    for i in range(m):
        total += a[i]*bb[i]
    ans += 1 if total>0 else 0
print(ans)