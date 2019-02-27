from fractions import gcd
n,k = map(int, input().split())
aa = list(map(int, input().split()))

gcd_aa = aa[0]
for a in aa[1:]:
    gcd_aa = gcd(gcd_aa, a)

print('POSSIBLE' if k<=max(aa) and k%gcd_aa==0 else 'IMPOSSIBLE')