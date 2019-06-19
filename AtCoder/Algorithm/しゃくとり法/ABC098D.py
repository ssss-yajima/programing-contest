'''
https://atcoder.jp/contests/abc098/tasks/arc098_b
'''
N = int(input())
A = list(map(int,input().split()))

li,ri = 0,0
ans = 0
xor = A[li]
add = A[li]
while ri < N and li <= ri:
    if xor == add:
        ans += ri - li +1
        ri += 1
        if ri < N:
            xor ^= A[ri]
            add += A[ri]
    else:
        if li < N:
            xor ^= A[li]
            add -= A[li]
        li += 1

print(ans)
