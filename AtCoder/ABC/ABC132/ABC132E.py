N,M = map(int,input().split())

route = [0]*N  # 通過済
connect=[[0]*N+1 for _ in range(N+1)]
edge = [(0,0) for _ in range(M)]

for i in range(M):
    u,v = map(int,input().split())
    edge[i][0] = u
    edge[i][1] = v
    connect[u][v] = 1
S,T = map(int,input().split())

def dfs(now, depth):
    # print("#"*depth,now, depth)
    # 通過済ならNG
    if route[now]: return 0
    # depth = Nなら達成
    if depth == N: return 1
    
    route[now] = 1
    ans = 0
    for i in range(N):
        if connect[now][i]:
            ans += dfs(i, depth+1)
    route[now] = 0
    return ans

min_length = dfs(S,T)
if min_length == 0:
    print(-1)
    quit()

# 最短経路の長さが3nの場合
if min_length % 3 ==0:
    print(min_length//3)
    quit()

# 往復できる場合
for u,v in edge:
    if connect[u][v] == 1 and connect[v][u]==1:
        print(min_length//3 + 1)
        quit()

# 閉路がある場合
for i in range(1,N+1):
    length = dfs(i,i)
    if length != 0 and length % 3 != 0:
        