n = int(input())
h = list(map(int,input().split()))

ans = 0
now = 0
for i in range(n-1):

    if h[i] >= h[i+1]:
        now += 1
        if now>ans:
            ans = now
    else:
        now = 0
print(ans)