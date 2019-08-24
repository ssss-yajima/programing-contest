n = int(input())
bb = list(map(int, input().split()))

while bb != []:
    for i in range(len(bb)):
        if bb[i] == i+1:
            print(bb.pop(i))
            break
    else:
        print(-1)
        break