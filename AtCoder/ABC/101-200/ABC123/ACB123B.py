import math
menu = sorted([int(input()) for _ in range(5)])
ans = 0
rest = 10
for a in menu:
    ans += math.ceil(a/10) * 10
    rest = rest if a%10==0 else min(rest, a%10)
# print(rest)
print(ans - 10 +  rest)
