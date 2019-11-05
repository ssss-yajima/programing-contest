import heapq
import math

n,m = map(int,input().split())
a = list(map(int,input().split()))

b = []
for ai in a:
    heapq.heappush(b, ai* -1)
# print(b)

for i in range(m):
    tmp = math.ceil(heapq.heappop(b)/2)
    heapq.heappush(b, tmp)
    # print(b)

print(sum(b) * -1)