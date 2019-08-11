import bisect
n,m = map(int,input().split())
ab = [[0] for _ in range(m)]
day_max = [0 for _ in range(m)]

for i in range(n):
    a,b = map(int,input().split())
    if a<= m:
        bisect.insort(ab[a-1],b)

for i in range(m):
    day_max[i] = ab[i][-1]
    if day_max[i] > 0:
        ab[i] = ab[i][0:-1]

# print(ab)
# print(day_max)

ans = 0
for day in range(m):
    gain = 0
    dayi = -1
    for i in range(day+1):
        if gain < day_max[i]:
            gain = day_max[i]
            dayi = i
    if dayi != -1:
        ans += day_max[dayi]
        day_max[dayi] = ab[dayi][-1]
        if day_max[dayi] > 0:
            ab[dayi] = ab[dayi][0:-1]
    # print(ans, day, dayi)

print(ans)
