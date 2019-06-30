N = int(input())
ABC = [list(map(int,input().split())) for _ in range(N)]

dp = [[0 for i in range(3)] for j in range(N)]

# 1日目の初期化
dp[0]= ABC[0]
for i in range(1,N):
    # 次ステップでA,B,Cに行く場合、
    for toi in range(3):
        s = 0
        # どこから来るのが最大か求める
        for fromi in range(3):
            # 同じ行動はとらない
            if toi==fromi:
                continue
            s = max(s, dp[i-1][fromi] + ABC[i][toi])
        dp[i][toi] = s

print(max(dp[-1]))
