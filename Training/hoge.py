# s = 'abcabcabc'

# target = 'c'
# idx = [i for i,x in enumerate(s) if x==target]
# print(idx)

# # targetより右側を揃えるまで
# print(len(s)-1 - idx[-1])

# for i in range(len(idx)-1):
#     idx[i+1] -= idx[i]
# # targetより左を揃えるまで
# print(idx)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
print(make_divisors(6))