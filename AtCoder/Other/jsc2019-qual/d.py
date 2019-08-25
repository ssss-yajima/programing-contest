n = int(input())

def b(x):
    return format(x,'04b')

for i in range(1,n+1):
    for j in range(i+1,n+1):
        tmp = i ^ j
        bit = format(tmp, 'b')[::-1]
        # print(bit)
        for k in range(len(bit)):
            # print(bit[k])
            if int(bit[k]) == 1:
                # print(bit, bit[k],k+1)
                print(k+1, end = ' ')
                break
    print()

        # print(b(i),b(j),b(tmp))

