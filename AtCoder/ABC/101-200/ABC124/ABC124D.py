n,k = map(int,input().split())
s = input()

arr = [0]
if s[0]=='0':
    arr.append(0)
for i in range(n-1):
    if s[i] != s[i+1]:
        arr.append(i+1)
arr.append(n)
if s[n-1] == '0':
    arr.append(n)
print(arr)

