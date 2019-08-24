n = int(input())
vv = list(map(int, input().split()))
cc = list(map(int, input().split()))

ans = 0
for i in range(n):
    if vv[i] > cc[i]:
        ans += vv[i]-cc[i]
print(ans)