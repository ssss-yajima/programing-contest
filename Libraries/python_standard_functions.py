### 標準入力
# 'aaa'
s = input()

# 3
n = int(input())

# ['aaa', 'bbb', 'ccc]
li = input().split()
# 1, 2
n,m = map(int, input().split())

# [['a','b','c'], ['a','b','c']]
xx = [input().split() for x in range(n)]
# [[1,2,3], [1,2,3]]
xx = [list(map(int,input().split())) for x in range(n)]

### 標準出力
# 0 padding
print('{:2.0f}'.format(x))
print('{:.2f}'.format(x))
# 配列を一気に出力
print(*xx, sep='\n')


### 初期化処理など
# 2次元配列の初期化
[[None] * n for _ in range(m)]

### 大域変数の使い方
x = 0
def func():
    global x
    x += 10

### 正規表現
import re
s='hoge6hoge21foo:bar'
re.findall(r'[a-z]+',s) #['hoge', 'hoge', 'foo', 'bar']
re.findall(r'[a-z0-9]+',s) # ['hoge6hoge21foo', 'bar']

### N進数
x = 255
print(bin(x))
print(oct(x))
print(hex(x))
print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))