
R,G,B,N = map(int,input().split())

ans = 0
for r in range(N//R+1):
    for g in range(N//G+1):
        b = (N-r*R-g*G)//B
        # print(r,g,b,r*R+g*G+b*B )
        if b>=0 and r*R+g*G+b*B == N:
            ans +=1
print(ans)