n = int(input())
P = list(map(int,input().split()))

ans = 0
for i in range(n-2):
    if P[i]<=P[i+1]<=P[i+2] or P[i+2]<=P[i+1]<=P[i]:
        ans += 1
print(ans)