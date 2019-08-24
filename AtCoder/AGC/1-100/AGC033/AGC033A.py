from collections import deque

h,w = map(int, input().split())
A = [[s for s in input()] for _ in range(h)]

visited = [[-1]*(w) for _ in range(h)]
dq = deque()
directions = [[0,1],[1,0],[0,-1],[-1,0]]

# 初期配置の黒をキューに追加
for hi in range(h):
    for wi in range(w):
        if A[hi][wi] == '#':
            dq.append([hi,wi])
            visited[hi][wi] = 0

# キューが空になるまで
while dq:
    hi,wi = dq.popleft()
    for d in directions:
        nhi, nwi = hi+d[0],wi + d[1]
        # 場外ならスキップ
        if nhi<0 or nhi>=h or nwi<0 or nwi>=w: continue 
        # 「黒くしてない白マス」をキューに追加
        if visited[nhi][nwi] == -1 and A[nhi][nwi] == '.':
            dq.append([nhi,nwi])
            visited[nhi][nwi] = visited[hi][wi] + 1

ans = -1
for x in visited:
    ans = max(ans,max(x))
print(ans)