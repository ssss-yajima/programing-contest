n,x = map(int,input().split())
aa = list(map(int, input().split()))
ans = 0
bits = format(x,'0{}b'.format(n))
# print(bits)
for i in range(n):
    ans += aa[i] if int(bits[::-1][i])==1 else 0
print(ans)