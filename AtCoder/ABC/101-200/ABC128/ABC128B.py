N = int(input())
# SP = sorted([list(input().split()) for _ in range(N)])
SP = {}
for i in range(N):
    city,score = input().split()
    if city in SP:
        SP[city].append([int(score),i])
    else:
        SP[city] = []
        SP[city].append([int(score),i])
# print(SP)


for city in sorted(SP.keys()):

    score = sorted(SP[city], reverse=True)
    for s in score:
        print(s[1]+1)
