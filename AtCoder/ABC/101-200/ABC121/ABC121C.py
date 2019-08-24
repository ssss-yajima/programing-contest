n,m = map(int, input().split())
shops = sorted([list(map(int,input().split())) for _ in range(n)])
rest = m
ans = 0
while rest > 0:
    shop = shops.pop(0)
    buy = min(rest, shop[1])
    ans += buy*shop[0]
    rest -= buy
print(ans)