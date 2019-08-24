N,K= map(int,input().split())
H = list(map(int,input().split()))

def calc_steps(fromi,toi):
    return abs(H[toi] - H[fromi])

costs = [0 for _ in range(N)]
# N <= Kのとき
if N <= K:
    K = N-1

# 最初のK段のコスト。O(K**2)
for toi in range(1,K+1):
    onestep = calc_steps(0, toi)
    nsteps = [costs[fromi] + calc_steps(toi,fromi) for fromi in range(1,toi)]
    costs[toi] = min([onestep] + nsteps)

# 計算済みK段から次の段へのコスト計算。O(KN)
# c1, c2, [c3,,,c3+k], next
for lasti in range(K,N):
    cost = 10**9
    for fromi in range(1,K+1):
        # 次の段へのコストは直近K段までのコスト ＋ その段からのコスト
        nsteps = costs[lasti - fromi] + calc_steps(lasti, lasti - fromi)
        cost = min(cost, nsteps)
    costs[lasti] = cost
    # print(costs)

print(costs[-1])
