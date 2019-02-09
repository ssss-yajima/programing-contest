s = int(input())

a = s
i = 1
aa=[s]
while i < 100000:
    i+=1
    if a%2 ==0:
        a = int(a / 2)
    else:
        a = int(a * 3 + 1)
    if aa.count(a)>0:
        print(i)
        break
    else:
        aa.append(a)