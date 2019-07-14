N = int(input())
A = list(map(int,input().split()))

cur = A[0]
for a in A[1:]:
    cur ^= a
# print(cur)
print('Yes' if cur==0 else 'No')