# D-Knapsack 1
N,W = map(int,input().split())
Weight = [0 for _ in range(N)]
Value = [0 for _ in range(N)]
for i in range(N):
    Weight[i],Value[i] = map(int,input().split())

MAX_N = 110
MAX_V = 100100

# dp[i+1][v]:= i番目までの品物の中からスコアがv以上になるように選んだときの、重さの総和の最小値
dp = [[10**15 for i in range(MAX_V)] for j in range(MAX_N)]
dp[0][0] = 0

for i in range(N):
    for sum_v in range(MAX_V):
        # i番目を選ぶ場合
        if sum_v - Value[i] >= 0:
            dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v - Value[i]] + Weight[i])

        # i番目を選ばない場合
        dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v])

ans = 0
# 重さの総和<=Wである最大スコアを探す
for sum_v in range(MAX_V):
    if dp[N][sum_v] <= W:
        ans = sum_v
print(ans)
