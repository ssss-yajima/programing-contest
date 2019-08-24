n = int(input())
aa = list(map(int, input().split()))
abs_aa = sorted([abs(a) for a in aa])
minus_count = sum([1 for a in aa if a < 0])
if minus_count % 2:
    abs_aa[0] *= -1
print(sum(abs_aa))