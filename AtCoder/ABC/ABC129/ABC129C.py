# fx = fx-1 + fx-2
N,M = map(int,input().split())
aa = [int(input()) for _ in range(M)]

oks = [True for _ in range(N)] + [False] + [False]
for a in aa:
    oks[a-1] = False
dp = [0]*(N+1)
dp[0]=1
# print(oks)
MOD = 10**9+7

for i in range(1,N+1):
    if i in aa:
        continue
    if i==1:
        dp[1] = dp[0]
        continue
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= MOD
print(dp[N])