import math
n,a,b = map(int, input().split())

if a>b:
    print(0)
elif n==1 and a != b:
    print(0)
else:
    print((b*(n-1)+a) - (a*(n-1)+b) +1 )
