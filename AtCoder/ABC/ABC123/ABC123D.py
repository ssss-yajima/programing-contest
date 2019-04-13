x,y,z,k = map(int, input().split())
aa = sorted(map(int, input().split()))
bb = sorted(map(int, input().split()))
cc = sorted(map(int, input().split()))
# 上のsortedがないとTLEする。
#  

ab = sorted(a+b for a in aa for b in bb)[:-k-1:-1]
abc = sorted(s+c for s in ab[:k] for c in cc)[:-k-1:-1]
print(*abc, sep='\n')
