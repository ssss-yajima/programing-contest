import math
n = int(input())
move = [int(input()) for _ in range(5)]
ans = 5 - 1 + math.ceil(n/min(move))
print(ans)