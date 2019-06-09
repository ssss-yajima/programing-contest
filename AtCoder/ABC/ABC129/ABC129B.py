n = int(input())
W = list(map(int,input().split()))
s = sum(W)
s1 = 0
ans = 10**5
for w in W:
    s1 += w
    s2 = s - s1
    ans = min(ans, abs(s1-s2))
print(ans)