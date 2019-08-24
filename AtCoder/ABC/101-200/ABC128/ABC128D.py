N,K = map(int,input().split())
V = list(map(int,input().split()))

take_count = min(N,K)
# とる個数
ans = -1 * 10**8
for i in range(1,take_count+1):
    drop_num = K-i # 捨てれる個数
    # 左からとる個数
    for li in range(i+1):
        take_left = V[:li]
        #　右からとる個数
        for ri in range(i+1-li):
            take = take_left
            take_right = []
            if ri>0:
                take_right =  V[-ri:]
            take = take_left + take_right
            take = sorted(take)
            # 捨てる
            for di in range(min(drop_num, len(take))):
                if take[di] < 0:
                    take[di] = 0
            ans = max(ans, sum(take))
            # print(i,li,ri,drop_num,ans,take_left,take_right,take,sum(take))
print(ans)