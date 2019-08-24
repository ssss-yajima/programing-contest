s = input()
zeroone = '01'* len(s)
onezero = '10' * len(s)
count_z = 0
count_o = 0
for i in range(len(s)):
    if s[i] == zeroone[i]:
        count_z += 1
    else:
        count_o += 1
print(min(count_o, count_z))