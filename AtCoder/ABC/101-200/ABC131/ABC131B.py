N,L = map(int,input().split())

taste = [L+i-1 for i in range(1,N+1)]
eat = min(map(abs,taste))
if L+N-1 < 0:
    eat *= -1

print(sum(taste) - eat)
