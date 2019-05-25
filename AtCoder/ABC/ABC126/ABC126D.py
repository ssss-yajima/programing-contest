N = int(input())
edge = [list(map(int,input().split())) for _ in range(N-1)]

ans = [0]* N
for e in edge:
    u,v,w = e
    # 長さが奇数の場合、頂点の白黒を分ける
    if w %2 == 1:
        ans[v-1] = int(not ans[u-1])
    else:
        ans[v-1] = ans[u-1]
for a in ans:
    print(a)