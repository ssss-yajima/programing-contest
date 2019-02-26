### A
n,k = map(int, input().split())
print('YES' if (n+1)//k >=2 else 'NO')

### B
aa=[list(map(int,input().split())) for _ in range(3)]

count=[0,0,0,0]
for i in range(1,5):
    for a in aa:
        count[i-1] += a.count(i)
print('YES' if count.count(0)==0 and count.count(3)==0 else 'NO')

### C
K,A,B = map(int, input().split())
rest = K- (A-1)
b=0
if rest>0:
    b = A + (B-A)*(rest//2) + rest%2
print(max(K+1, b))