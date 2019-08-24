import sys
import math
sys.setrecursionlimit(1000000)

N,blue = map(int,input().split())
red = N-blue
MOD = 10**9+7

def cmb(n, r):
    ans = (math.factorial(n) // math.factorial(n-r)) // math.factorial(r)
    return ans

# 操作回数
for i in range(1, blue+1):
    if red +1 -i >= 0: # 赤の隙間と両端
        # 青の差し込み箇所（操作回数）
        ins_ptn = cmb(red+1, i) % MOD
        # 青の配置方法
        layout_ptn = cmb(blue-1, i-1) % MOD
        print(ins_ptn * layout_ptn % MOD)
    else:
        print(0)