n,c,k = map(int, input().split())
tt = sorted([int(input()) for _ in range(n)])
# print(tt)
ans = 0
limit = 0
buss = 1
for i,t in enumerate(tt):
    if buss == c or t>limit:
        # print('NEED MORE BUSS')
        ans += 1
        buss = 1
        limit = t+k
    else:
        buss +=1
    # print(ans, buss, t, limit)
print(ans)