n,x = map(int,input().split())
L = list(map(int,input().split()))
ans = 1
pos = 0
for l in L:
    pos += l
    if pos <= x:
        ans +=1
print(ans)