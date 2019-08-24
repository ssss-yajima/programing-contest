n,k = map(int,input().split())
a = list(map(int,input().split()))
MOD = 10**9+7

cnt_a = 0
cnt_b = 0
for i in range(n-1):
    for j in range(i+1,n):
        cnt_a += 1 if a[i] > a[j] else 0
        cnt_b += 1 if a[i] < a[j] else 0
ans = cnt_a * (1+k)*k//2
ans += cnt_b * (1+k-1)*(k-1)//2

# print(cnt_a)
print(ans%MOD)