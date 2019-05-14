n = int(input())

# 約数を列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
ans = 0
divisors = make_divisors(n)
for x in divisors:
    tmp = x-1
    if tmp>0 and n//tmp == n%tmp:
        ans += tmp
print(ans)