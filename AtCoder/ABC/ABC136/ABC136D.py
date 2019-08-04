import math
S = input()

ans = [0 for _ in range(len(S))]
current_char = 'R'
pos_RL = -1
count = 0

for i in range(len(S)):
    if S[i] == current_char:
        count += 1
        # print('#',count,ans,i,current_char)
    else:
        if current_char == 'R':
            current_char = 'L'
            pos_RL = i-1
            ans[pos_RL+1] += math.floor(count/2)
            ans[pos_RL] += math.ceil(count/2)
        else:
            current_char = 'R'
            ans[pos_RL] += math.floor(count/2)
            ans[pos_RL+1] += math.ceil(count/2)
        # print('$',count,ans,i,current_char)
        count = 1
        
if current_char == 'R':
    current_char = 'L'
    pos_RL = i-1
    ans[pos_RL+1] += math.floor(count/2)
    ans[pos_RL] += math.ceil(count/2)
else:
    current_char = 'R'
    ans[pos_RL] += math.floor(count/2)
    ans[pos_RL+1] += math.ceil(count/2)


for a in ans:
    print(a, end=' ')
print()