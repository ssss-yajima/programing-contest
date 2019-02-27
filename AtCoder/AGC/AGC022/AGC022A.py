import bisect
ss = input()
ss =list(map(ord, ss))
dic = [i for i in range(97,123)]
# print(dic)
for s in ss:
    dic.remove(s)
# print(dic)
if len(ss)<26:
    ss.append(min(dic))
else:
    for s in ss[::-1]:
        if len(dic)>0 and s < max(dic):
            ss[ss.index(s)] = dic[bisect.bisect_right(dic,s)]
            break
        dic.append(ss.pop(ss.index(s)))
        dic = sorted(dic)
    else:
        ss = -1
print(ss if ss == -1 else ''.join(list(map(chr,ss))))