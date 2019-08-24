n=int(input())
ans=0
for i in range(n):
    x,u = input().split()
    if u =='BTC':
        x = float(x)*380000
    ans+=float(x)
print(ans)