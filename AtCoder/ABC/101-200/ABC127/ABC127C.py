n,m =map(int,input().split())
gates = [list(map(int,input().split())) for _ in range(m)]

l=0
r = 10**9
for g in gates:
    l = max(l, g[0])
    r = min(r, g[1])
print(r-l+1 if r>=l else 0)