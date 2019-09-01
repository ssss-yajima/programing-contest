n = int(input())
a = [list(map(lambda x:x-1,map(int,input().split()))) for _ in range(n)]

game_count = [0 for _ in range(n)]
ans = 0
remaining_games = n * (n-1) //2
last_remains = remaining_games
while(remaining_games>0):
    done = [False for _ in range(n)]
    for playeri in range(n):
        if game_count[playeri] >= n-1:
            done[playeri] = True
            continue

        # print(f'day:{ans} p:{playeri} games:{game_count[playeri]} done:{done[playeri]} ', end='')

        rival = a[playeri][game_count[playeri]]
        if done[playeri] or done[rival]:
            print()
            continue

        # print(f'rival:{rival}')
        if a[rival][game_count[rival]] == playeri: #match
            game_count[playeri] += 1
            game_count[rival] += 1
            done[playeri] = True
            done[rival] = True
            remaining_games -= 1
    ans += 1
    if last_remains == remaining_games:
        print(-1)
        break
else:
    print(ans)