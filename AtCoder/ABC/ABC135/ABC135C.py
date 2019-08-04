N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
for i in range(N):
    if A[i] <= B[i]:
        ans += A[i]
        B[i] -= A[i]
        A[i] = 0

        ans += min(A[i+1], B[i])
        A[i+1] = max(0, A[i+1] - B[i])
    else:
        ans += B[i]
        A[i] -= B[i]
print(ans)