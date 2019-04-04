n,q = map(int,input().split())
s = input()
magic = [list(input().split()) for _ in range(q)]

s = '+' + s + '*'

def move(start_idx):
    idx = start_idx
    char = s[idx]
    for m in magic:
        if m[0] == char and 1 <= idx <= n:
            idx += 1 if m[1]=='R' else -1
            char = s[idx]
    return idx

# 二分探索（左に消える場合）
target = s
idx = 0
while len(target)>1:
    mid = len(target)//2
    if move(mid) == 0:
        target = target[mid:]
        idx += mid  
    else:
        target = target[:mid]
        idx -= mid
    print(idx, target)
print("Left ",idx,target)

target = s
idx = 0
while len(target)>1:
    mid = len(target)//2
    if move(mid)== len(s):
        target = target[:mid]
        idx -= mid  
    else:
        target = target[mid:]
        idx += mid
    print(idx, target)
print("Right",idx,target)

print(s)
# for i in range(1,n+1):
#     print(i, move(i))