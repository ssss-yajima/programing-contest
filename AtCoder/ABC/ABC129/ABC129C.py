import math

def combnation(x,y):
    return math.factorial(x) // (math.factorial(x-y) * math.factorial(y))


N,M = map(int,input().split())
aa = [0] + [int(input()) for _ in range(M)] + [N]

DIV = 10**9+7

ans = 1
a_prev = aa[0]
for a in aa[1:]:
    steps = a - a_prev -1
    if steps == 0 and a_prev>0 and a < aa[-1]:
        ans = 0
        break
    tmp = 0
    for i in range(steps//2 + 1):
        
        tmp += combnation(steps-i, i)
        # print(ans, tmp,combnation(steps-i, i), i, steps, a_prev, a)
    a_prev=a
    ans = ans*tmp
    # print('-'*10)
# print(ans)
print(ans%DIV)