a,b = map(int,input().split())
if abs(a-b)%2 == 1:
    print('IMPOSSIBLE')
else:
    print(max(a,b) - abs(a-b)//2)