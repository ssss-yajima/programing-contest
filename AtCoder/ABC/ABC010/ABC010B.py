n = int(input())
aa = list(map(int, input().split()))
oks = [1,3,7,9]
ans = 0
for a in aa:
    if oks.count(a) == 0:
        for ok in oks[::-1]:
            if ok<a:
                ans += a - ok
                break
print(ans)
