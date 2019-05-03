# ユークリッドの互除法
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def gcd_for_list(target_list, begin_idx, end_idx):
    ans = 0
    for x in target_list[begin_idx:end_idx]:
        ans = gcd(ans,x)
    return ans

n = int(input())
aa = list(map(int, input().split()))


ans = 1

for i in range(n+1):
    left = aa[:i]
    right =aa[i+1:]
    print(left,right)