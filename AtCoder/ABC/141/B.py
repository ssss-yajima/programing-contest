s = input()
odd = {'R', 'U','D'}
even = {'L', 'U', 'D'}

for si in range(len(s)): 
    if (si+1) % 2 == 0 and s[si]=='R' or (si+1)%2==1 and s[si]=='L':
        print('No')
        break
else:
    print('Yes')