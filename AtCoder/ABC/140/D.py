n,k = map(int,input().split())
s = input()

ans = 0
switch = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        ans += 1
    else:
        switch += 1
ans += min(k,switch) * 2
print(min(n-1, ans))