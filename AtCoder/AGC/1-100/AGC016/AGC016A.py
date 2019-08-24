from collections import Counter
ss = input()

ans = 1000
candidates = set(ss)
for s in candidates:
    count = 0
    t = list(ss)
    while True:
        if len(set(t))==1:
            ans = min(ans, count)
            break
        t = [t[i] if t[i+1] != s else t[i+1] for i in range(len(t)-1)]
        count += 1
print(ans)