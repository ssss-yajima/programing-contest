n = int(input())
s = input()
t = input()

ans = 2*n
for i in range(n+1)[::-1]:
    if s[-i:] == t[:i]:
        ans -= i
        break
print(ans)