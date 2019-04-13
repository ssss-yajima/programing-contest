n,k = map(int,input().split())
s = input()

last_char = s[0]
streak = 1
count = 0
arr = [0]* (n)
for i in range(n):
    if i== n-1:
        arr[count] = streak if s[i] == '1' else -streak
        break
    if s[i] != s[i+1]:
        arr[count] = streak if s[i] == '1' else -streak
        streak = 0
        count += 1
    streak += 1

ans = 0
cur = 0
rest = k
current_arr = []
for i in range(n):
    if rest == 0 and arr[i]<0: # remove top
        cur -= current_arr.pop(0)
        rest += 1
    if arr[i] < 0:
        rest -= 1
    current_arr.append(abs(arr[i]))
    cur += abs(arr[i])
    ans = max(ans, cur )
    print(i,rest, arr[i],cur, ans, current_arr)
    if arr[i] == 0: break