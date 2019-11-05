n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

ans = 0
tmp = -10
for ai in a:
    ans += b[ai-1]
    if tmp+1 == ai:
        ans += c[tmp-1]
    tmp = ai
    # print(ans)
print(ans)