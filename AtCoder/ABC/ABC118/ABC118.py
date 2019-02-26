# #A
a,b = map(int,input().split())

print((a+b) if b%a==0 else (b-a))

#B
n,m = map(int,input().split())
aa = []
kk=[]
for i in range(n):
    tmp = list(map(int,input().split()))
    kk.append(tmp[0])
    aa.append(tmp[1:])

aaa = []
for a in aa:
    for ai in a:
        aaa.append(ai)
ans=0
for i in range(m):
    if aaa.count(i+1)==n:
        ans+=1
print(ans)

#C
n = int(input())
aa = list(map(int,input().split()))

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

ans=aa[0]
for i in range(1,n):
    ans = gcd(ans, aa[i])
print(ans)