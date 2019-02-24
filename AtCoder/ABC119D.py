import bisect
A,B,Q = map(int, input().split())
INF = 10**18
ss = [-INF] + [int(input()) for _ in range(A)] + [INF]
tt = [-INF] + [int(input()) for _ in range(B)] + [INF]
xx = [int(input()) for _ in range(Q)] 
for x in xx:
    b = bisect.bisect_right(ss, x)
    d = bisect.bisect_right(tt, x)
    ans=INF
    for s in [ss[b-1], ss[b]]:
        for t in [tt[d-1], tt[d]]:
            d1 = abs(s - x) + abs(t - s)
            d2 = abs(t - x) + abs(s - t)
            ans = min(ans, d1,d2)
    print(ans)
            