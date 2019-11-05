n,k,q = map(int,input().split())
a = [int(input()) for _ in range(q)]

minus = [q for _ in range(n)]
for ai in a:
    minus[ai-1] -= 1

for i in range(n):
    if (minus[i] >= k):
        print('No')
    else:
        print('Yes')

