'''
https://atcoder.jp/contests/abc038/tasks/abc038_c
'''
N = int(input())
A = list(map(int, input().split()))

ri,li = 0,0
ans = 0
last = -1   # OKになった最後尾の値
# current = []
while(ri < N and li <= ri):
    # 条件を満たす限り右に進める
    if last <A[ri]:
        last = A[ri]
        ri += 1
    # 条件を満たさなくなったとき、それまでの長さからans加算
    else:
        ans += sum([i+1 for i in range(ri-li)])
        li = ri
        last = A[ri]
        ri += 1
ans += sum([i+1 for i in range(ri-li)])

print(ans)
