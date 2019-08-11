n = int(input())
sn = sorted([''.join(sorted(input())) for _ in range(n)])

ans = 0
cnt = 1
for i in range(n-1):
    # print(sn[i], cnt, ans)
    if sn[i] == sn[i+1]:
        cnt += 1
    else:
        ans += cnt * (cnt -1) //2
        cnt = 1
ans += cnt * (cnt -1) //2
print(ans)
