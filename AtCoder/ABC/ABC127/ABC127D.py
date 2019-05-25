import bisect
N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
BC = [list(map(int,input().split())) for _ in range(M)]

print(BC)
print(sorted(BC, key = lambda x:x[1] , reverse=True))

BC = sorted(BC, key = lambda x:x[1] , reverse=True)

ans = 0
changed_idx = 0
# 数値の大きい順に処理
for bc in BC:
    # 二分探索
    idx = bisect.bisect_right(A,bc[1])
    idx = min(idx, bc[0])
    if idx > changed_idx:
        ans += bc[1] * (idx - changed_idx)
        changed_idx = idx
    print('bd:{} idx:{} ans:{} changed_idx:{}'.format(bc, idx, ans, changed_idx))
rest = A[changed_idx:]
ans += sum(rest)

print(ans)