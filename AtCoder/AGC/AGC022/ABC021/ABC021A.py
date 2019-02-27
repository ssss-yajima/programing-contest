n = int(input())
digit = len(str(n))
ans = int(str(n)[0])
if digit > 1:
    ans += 9 * (digit - 1)
    if int(str(n)[1:]) < (10 ** (digit-1) - 1):
        ans -= 1
print(ans)