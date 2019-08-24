n = int(input())
aa = list(map(int, input().split()))

bin = list(map(lambda x:x%2, aa))
even = bin.count(1)
print('YES' if even%2==0 else 'NO')