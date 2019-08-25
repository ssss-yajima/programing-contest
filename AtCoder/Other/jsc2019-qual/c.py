import math
n = int(input())
s = input()
MOD = 10**9+7

lr = [False] * 2*n
lr[0] = True # True:Left False:Right
for i in range(1,2*n):
    lr[i] = not lr[i-1] if s[i-1] == s[i] else lr[i-1]

if s[0] == 'W':
    lr = lr[1:]
if s[-1] == 'W':
    lr = lr[:-1]

ans = 1
lCnt = 0
for i in range(len(lr)):
    if not lr[i]: # R
        ans *= lCnt
        lCnt -= 1
    else:       # L
        lCnt += 1
print(math.factorial(n) * ans % MOD) 