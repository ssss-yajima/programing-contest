n = int(input())
ans = 4**n
if n>= 3:
    ans -= 3 * (n-2)*4**(n-3)
if n>= 4:
    ans -= 2  *(n-3) * 4**(n-4)
    
print(ans%(10**9+7))