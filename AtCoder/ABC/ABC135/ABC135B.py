N = int(input())
pn = list(map(int,input().split()))
pn_sort = sorted(pn)

cnt = 0
for i in range(N):
    if pn[i] != pn_sort[i]:
        cnt +=1
if cnt>2:
    print('NO')
else:
    print('YES')