n = int(input())

ww = [input() for _ in range(n)]
# print(ww)

for i,w in enumerate(ww[:-1]):
    if ww[i][-1] != ww[i+1][0] or ww.count(w)>1:
        print('No')
        # print(w)
        break
else:
    print('Yes')