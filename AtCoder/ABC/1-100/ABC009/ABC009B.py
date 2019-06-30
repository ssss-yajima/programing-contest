n = int(input())
aa = [int(input()) for _ in range(n)]
print(max([x for x in aa if x < max(aa)]))