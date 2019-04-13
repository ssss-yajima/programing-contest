a,b = map(int, input().split())
ans = max(a,b)
if a>b:
    a-=1
else:
    b-=1
print(ans + max(a,b))