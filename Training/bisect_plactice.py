import bisect
ll = [2,3,4,6,8,16]

idx = bisect.bisect_left(ll, 3)
print(idx, ll[idx])
