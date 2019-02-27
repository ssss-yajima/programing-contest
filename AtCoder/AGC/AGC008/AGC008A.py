x,y = map(int, input().split())
if y==0:
    ans = abs(x) + (x>0)
else:
    ans = abs(abs(x)-abs(y))
    if x>=0 and y>=0:
        if x>y:
            ans +=2
    elif x<0 and y<0:
        if x>y:
            ans += 2
    else:
        ans +=1
print(ans)