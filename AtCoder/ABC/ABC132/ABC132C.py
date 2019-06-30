N = int(input())
D = sorted(list(map(int,input().split())))

mid = N//2
# print(D)
print(D[mid] - D[mid-1])
