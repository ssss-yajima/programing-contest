import math
n = int(input())
move = [int(input()) for _ in range(5)]
ans = 4 + math.ceil(n/min(move))
print(ans)