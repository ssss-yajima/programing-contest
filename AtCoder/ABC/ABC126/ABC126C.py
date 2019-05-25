import math
from math import log2
from math import ceil

N,K = map(int,input().split())

def prob_wins(x,k):
    if x>=k:
        return 1
    return 0.5**ceil(log2(k/x))

ans = 0
for i in range(1,N+1):
    ans += prob_wins(i,K)
    # print(i,prob_wins(i,K))
print(ans/N)