N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB = sorted(AB, key=lambda x:x[1])

time_spent = 0
for a,b in AB:
    time_spent += a
    if time_spent > b:
        print('No')
        break
else:
    print('Yes')