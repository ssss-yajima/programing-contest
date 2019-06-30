# D-Knapsack 1
N,W = map(int,input().split())
Weight = [0 for _ in range(N)]
Value = [0 for _ in range(N)]
for i in range(N):
    Weight[i],Value[i] = map(int,input().split())

# dp[i+1][w]:= i番目までの品物の中から重さがwを超えないように選んだときの、価値の総和の最大値
dp = [[0 for i in range(W+1)] for j in range(N+1)]

for i in range(N):
    # あらゆる合計重量sum_wに対して品物iを入れるべきか計算する
    for sum_w in range(W+1):
        # i番目を選ぶ場合
        if sum_w - Weight[i] >= 0:
            dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w - Weight[i]] + Value[i])

        # i番目を選ばない場合
        dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w])

# for d in dp:
#     print(d)

print(dp[N][W])
