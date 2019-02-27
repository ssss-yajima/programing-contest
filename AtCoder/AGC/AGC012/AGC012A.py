n = int(input())
aa = list(map(int, input().split()))
xx = sorted(aa)[n::2]
# print(xx)
print(sum(xx))