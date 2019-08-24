from collections import deque
N,K = map(int,input().split())
A = list(map(int,input().split()))

ri = 0
li = 0
sum = A[0]
ans=0
while(ri < N and li<N):
    if sum < K:
        ri += 1
        sum += A[ri]
    else:
        sum -= A[li]
        ans += 1
        li += 1
    print(f'li:{li} ri:{ri} sum:{sum} ans:{ans}')
print(ans)