n = int(input())
aa = list(map(int, input().split()))

if n==1:
    print(1)
else:
    mode = None
    ans = 1
    for i in range(n-1):
        if aa[i] != aa[i+1]:
            if mode == None:
                mode = aa[i]<aa[i+1]
            elif (aa[i] < aa[i+1]) != mode:
                ans+=1
                mode = None
        # print(aa[i], aa[i+1], aa[i]<aa[i+1],  mode, ans)
    print(ans)
