import bisect

n,m = map(int,input().split())
a = list(map(int,input().split()))

b = []
for ai in a:
    bisect.insort(b,ai )
# print(b)

for i in range(m):
    tmp = b.pop()//2
    bisect.insort(b, tmp)
    # print(b)

print(sum(b))