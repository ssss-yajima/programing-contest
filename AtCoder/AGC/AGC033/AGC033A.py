from collections import deque

h,w = map(int, input().split())
A = [['*']*(w+2)] + [['*']+[s for s in input()]+['*'] for _ in range(h)] + [['*']*(w+2)]

dist_to_black = [[0]*w for _ in range(h)]

# # debug
# for a in A:
#     print(a)
# for a in dist_to_black:
#     print(a)

def bfs(sy,sx):
    dq = deque([(sy,sx,0)])
    while dq:
        y,x,n = dq.popleft()
        if A[y][x]=='#':
            return n
        elif A[y][x]=='.':
            dq.append([y+1,x,n+1])
            dq.append([y-1,x,n+1])
            dq.append([y,x+1,n+1])
            dq.append([y,x-1,n+1])

ans = -1
for i in range(h):
    for j in range(w):
        # dist_to_black[i][j] = bfs(i+1,j+1)
        ans = max(ans, bfs(i+1, j+1))

print(ans)