m,d = map(int,input().split())

ans = 0
for mi in range(1,m+1):
    for di in range(1,d+1):
        if di<10: continue
        di1 = di%10
        di10 = di//10
        if di1 >=2 and di10>=2 and di1*di10==mi:
            ans += 1
        # print(mi,di10,di1, di, ans)
print(ans) 
