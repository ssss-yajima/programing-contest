n = int(input())
aa = [0]*n
bb = [0]*n
for i in range(n):
    aa[i],bb[i] = map(int, input().split())
ans = 0
for i in range(1,n+1):
    cnt = 0
    cur = aa[-i] + ans
    if cur % bb[-i] > 0:
        cnt = ((cur - 1) // bb[-i] +1) * bb[-i] - cur
        # print(cur, bb[-i], cnt, aa)
        ans += cnt
    
print(ans)