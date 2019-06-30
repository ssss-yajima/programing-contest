s = input()
t = input()
replace = ['a','t','c','o','d','e','r']
for i in range(len(s)):
    if (s[i]=='@' and replace.count(t[i])>0) \
    or (t[i]=='@' and replace.count(s[i])>0) \
    or s[i]==t[i]:
        continue
    else:
        print('You will lose')
        break
else:
    print('You can win')