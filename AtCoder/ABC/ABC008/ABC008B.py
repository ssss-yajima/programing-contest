n = int(input())
ss = [input() for _ in range(n)]

ans = ''
border = -1
for s in set(ss):
    if ss.count(s) > border:
        border = ss.count(s)
        ans = s
print(ans)