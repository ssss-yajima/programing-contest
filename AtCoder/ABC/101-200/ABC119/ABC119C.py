N,A,B,C = map(int, input().split())
ll = [int(input()) for _ in range(N)]
INF = 10**9
# 再帰で全組み合わせのコストを計算する
def dfs(cur,a, b, c):
    # 全部の竹を使ったらコストを返す
    if cur == N:
        return abs(A-a)+abs(B-b)+abs(C-c)-30 if min(a,b,c)>0 else INF
    ret0 = dfs(cur+1, a,b,c) # 使わない場合
    ret1 = dfs(cur+1, a+ll[cur],b,c)+10 # Aに使う場合
    ret2 = dfs(cur+1, a,b+ll[cur],c)+10 # Bに使う場合
    ret3 = dfs(cur+1, a,b,c+ll[cur])+10 # Cに使う場合
    return min(ret0,ret1,ret2,ret3)
print(dfs(0,0,0,0))