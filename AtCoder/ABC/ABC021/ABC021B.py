n = int(input())
a,b = map(int, input().split())
k = int(input())
pp = list(map(int, input().split()))
pp.append(a)
pp.append(b)
print('YES' if len(set(pp))==len(pp) else 'NO')
