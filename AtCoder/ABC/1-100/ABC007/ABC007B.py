a = list(input())
# print(a)
# a = list(map(ord, a))
if a == ['a']:
    print(-1)
else:
    for i in range(1,len(a)+1):
        if a[-i] != 'a':
            a[-i] = chr(ord(a[-i])-1)
            break
        else:
            a[-i] = ''
            break
    print(''.join(a))
