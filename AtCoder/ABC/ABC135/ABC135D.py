import re
S = input()

targets = []
for i in range(10**len(S) // 13):
    targets.append(i*13 + 5)
# print(targets)

regs = [S]
for i in range(len(S)-1):
    if S[i] == '?':
        regs.append(S[i+1:])
    else:
        break

# print(regs)

for i in range(len(regs)):
    regs[i] = '^' + regs[i].replace('?', '\d') + '$'
# print(regs)

ans = 0
for t in targets:
    for reg in regs:
        if re.match(reg, str(t)):
            ans += 1
            ans %= (10**9+7)
        # print(ans, t)

print(ans)