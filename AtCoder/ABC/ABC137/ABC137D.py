import heapq
import bisect

n,m = map(int,input().split())
ab = [[0,0,0] for _ in range(n)]

for i in range(n):
    a,b = map(int,input().split())
    # 優先度付きキューが最小値をpopするため、最大価値の負の値をKeyとする
    ab[i] = [-b,a,b]

# 日付でソート
ab = sorted(ab, key=lambda x:x[1])

# print(ab)

day = 1
# ans = []
ans = 0
pqueue = []

for i in range(n):
    if ab[i][1] > m:
        break

    # 同じ必要日数のタスクをpush
    if ab[i][1] <= day:
        heapq.heappush(pqueue, ab[i])
    else:
        # タスクの必要日数が変わったら日付を更新
        # その日付までに処理可能な最も価値のある仕事を回答に加算
        for j in range(day, ab[i][1]):
            if len(pqueue) > 0:
                ans += heapq.heappop(pqueue)[2]
                # ans += [heapq.heappop(pqueue)[2]] // debug
                day = ab[i][1]
        # 次の日付の要素をpush
        heapq.heappush(pqueue, ab[i])
    # print(f"i:{i} day:{day} ans:{ans} queue:{pqueue}")

for k in range(day, m+1):
    if len(pqueue) > 0:
        ans += heapq.heappop(pqueue)[2]
        # ans += [heapq.heappop(pqueue)[2]] //debug
        # print(f"## i:{i} day:{k} ans:{ans} queue:{pqueue}")

print(ans)
