a,b,c,d = map(int,input().split())

# ユークリッドの互除法
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd (a, b)

cd = lcm(c,d)

mul_count = b//c + b//d - b//cd
a -= 1
mul_count -= (a//c + a//d -a//cd)
print(b - a - mul_count)

# print(cd)
# print(b//c ,b//d ,b//cd)
# print(a//c ,a//d ,a//cd)
