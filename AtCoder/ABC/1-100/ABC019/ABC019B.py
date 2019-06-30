s = input()
cur = s[0]
count = 1
for i,x in enumerate(s[1:]):
    if cur==x:
        count+=1
    else:
        print('{}{}'.format(cur,count), end='')
        count=1
        cur = x
print('{}{}'.format(cur,count))