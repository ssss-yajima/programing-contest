n = int(input())

while n>=4 or n==0:
    if n% 4 ==0:
        print('Yes')
        break
    n-=7
else:
    print('No')