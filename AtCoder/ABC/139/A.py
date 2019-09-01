s = input()
t = input()
ans = 0
for i in range(3):
    ans += 1 if s[i] == t[i] else 0
print(ans)