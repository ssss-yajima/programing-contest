import math
n = int(input())
ans = 0
for x in range(1,n+1):
    if((1+math.floor(math.log10(x)))%2 == 1):
        ans += 1
print(ans)