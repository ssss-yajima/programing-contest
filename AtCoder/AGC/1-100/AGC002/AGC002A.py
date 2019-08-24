a,b = map(int,input().split())
if a*b<0:
    print('Zero')
elif 0<a:
    print('Positive')
else:
    neg_range = min(-1,b) - a +1
    if neg_range%2==0:
        print('Positive')
    else:
        print('Negative')