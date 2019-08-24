n = int(input())
s = input()

lr = [False] * 2*n
lr[0] = True # True:Left False:Right
for i in range(1,2*n):
    lr[i] = not lr[i-1] if s[i-1] == s[i] else lr[i-1]

for i in range(2*n):
    print("L" if lr[i] else "R", end="")

ans = 1
lCnt = 0
for i in range(2*n):
    if not lr[i]: # R
        ans *= lCnt
    else:       # L
        lCnt += 1

print(ans) 