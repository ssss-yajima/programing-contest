xx = input()

remove = 0
s_num=0
for x in xx:
    if x=='S':
        s_num += 1
    else:
        if s_num>0:
            remove += 1
            s_num -= 1
print(len(xx) - 2 * remove)