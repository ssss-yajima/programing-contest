s = input()
target = ['A','C','G','T']
ans = []
count = 0
for x in s:
    if target.count(x)>0:
        count += 1
    else:
        if count >0:
            ans.append(count)
            count = 0
print(max(ans+[count]))