a,b,k = map(int,input().split())

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

ans =[]
for x in range(1, gcd(a,b)+1):
    if a%x==0 and b%x==0:
        ans.append(x)
# print(ans)
print(ans[-k])