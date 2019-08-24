N = int(input())
A = list(map(int,input().split()))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

cnt = 0
ans = [0] * (N+1)
digits = [0] * (N+1)
for i in range(N,0,-1):
    ans[i] = digits[i]%2 ^ A[i-1]
    cnt += ans[i]
    divs = make_divisors(i)
    for div in divs:
        digits[div] += ans[i]
    
# print(digits)
# print(ans)
print(cnt)
for a in ans[1:]:
    if cnt <= 0:
        break
    print(a)
    cnt -= a