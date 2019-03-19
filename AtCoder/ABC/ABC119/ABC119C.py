import itertools
n,a,b,c = map(int, input().split())
ll = [int(input()) for _ in range(n)]

# A,B,C,NotUsed
group =[[] for _ in range(4)]

print(list(itertools.product(ll,repeat=4)))
print(len(list(itertools.product(ll,repeat=4))))