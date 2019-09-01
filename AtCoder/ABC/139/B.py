a,b = map(int,input().split())

ans = 0
tap = 1
while tap<b:
    tap -=1
    tap +=a
    ans += 1
print(ans)