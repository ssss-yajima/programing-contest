import itertools
N,M = map(int,input().split())
K = [0]*M
S = [[0] *N for _ in range(M)]
for i in range(M):
    tmp = list(map(int,input().split()))
    K[i] = tmp[0]
    for s in tmp[1:]:
        S[i][s-1] = 1
P = list(map(int,input().split()))

ptns = list(itertools.product((0,1),repeat=N))
ans = 0
# 全てのON/OFFパターン
for p in ptns:
    # 全ての電球
    for i in range(M):
        # ONになっているスイッチ
        on_count = 0
        for j in range(N):
            on_count += S[i][j] and p[j]
        if on_count%2 != P[i]:
            break
        
    else:
        # print(p)
        ans += 1
print(ans)
