n,q = map(int,input().split())
s = input()
magic = [list(input().split()) for _ in range(q)]

mapping = [[] for _ in range(27)]
positions = [0] * (n + 2) #ゴミ置き場を両端に追加
# 位置ごとの個数と文字ごとの配列位置
for i in range(n):
    mapping[ord(s[i])-65].append(i+1)
    positions[i+1] += 1
# print(positions)      ##
# print(mapping)  ##

for m in magic:
    order = 1 if m[1] == 'L' else -1
    for idx in mapping[ord(m[0])-65][::order]:
        positions[idx-order] += positions[idx]
        positions[idx] = 0
    # print(m,positions)
print(sum(positions[1:-1]))