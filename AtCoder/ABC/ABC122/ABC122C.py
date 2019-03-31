n,q = map(int, input().split())
s = input()
lr = [list(map(lambda x: int(x)-1, input().split())) for _ in range(q)]

ac = [0]*n
for i in range(n-1):
    if s[i:i+2] == 'AC':
        ac[i+1]= ac[i]+1
    else:
        ac[i+1] = ac[i]
for x in lr:
    print(ac[x[1]] - ac[x[0]])