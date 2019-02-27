a,b,c = map(int, input().split())

if a%2==1 or b%2==1 or c%2 ==1:
    print(0)
elif a==b==c:
    print(-1)
else:
    ans=0
    while a%2==0 and b%2==0 and c%2==0:
        x = (b+c)//2
        y = (a+c)//2
        z = (a+b)//2
        a=x
        b=y
        c=z
        ans+=1
    print(ans)