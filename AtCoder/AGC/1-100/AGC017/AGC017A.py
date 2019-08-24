import math
n,p = map(int, input().split())
aa = list(map(int, input().split()))

aa = list(map(lambda x:x%2, aa))
odd = aa.count(1)
even = aa.count(0)
ans = 2**even
# if p==1:
#     ans*=odd
#     odd-=1
# 偶数個の選び方
pattern = 0
for i in range(p, odd+1, 2):
    # print(even, odd, i, math.factorial(odd) // (math.factorial(i)*math.factorial(odd-i)))
    pattern += math.factorial(odd) // (math.factorial(i)*math.factorial(odd-i))
print(ans*pattern)