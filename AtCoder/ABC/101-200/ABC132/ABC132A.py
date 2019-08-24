s = input()
if len(list(set(s))) == 2:
    if s.count(s[0])==2:
        print('Yes')
else:
    print('No')