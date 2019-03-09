a,b = map(int,input().split())

ans = 0
length = b-a+1
if a%2 != 0:
    ans = ans^a
if b%2 == 0:
    length -= 1
    ans = ans^b
pair_count= length//2
ans = ans^(pair_count%2)
print(ans)