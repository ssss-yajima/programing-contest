n = int(input())
s = input()

ans = 0
for i in range(1,n+1):# length of term
    for j in range(n-i+1):# start pos
        if len(s[j:j+i]) == len(list(set(s[j:j+i]))):
            ans += 1
        print(i,j,s[j:j+i], ans)
print(ans)