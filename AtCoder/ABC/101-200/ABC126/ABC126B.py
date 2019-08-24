s = input()
l = int(s[:2])
r = int(s[2:])

if 1<=l<=12 and 1<=r<=12:
    print('AMBIGUOUS')
elif 1<=l<=12 and (r==0 or 12<r):
    print('MMYY')
elif (l==0 or 12<l) and 1<=r<=12:
    print('YYMM')
else:
    print('NA')
