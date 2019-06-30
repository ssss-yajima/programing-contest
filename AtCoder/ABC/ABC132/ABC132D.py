N,blue = map(int,input().split())
red = N-blue

def cmb(n, r):
    nCr = {}
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

# 操作回数
max_opr = min(red+1, blue)

print(max_opr)
print(blue,red)

for insi in range(max_opr):
    # 差し込み方
    slice_cnt = cmb(blue-1,insi)

    red_cnt = 0
    # 外で使う数
    for j in range(red-insi):
        if insi ==0: # 全部外
            red_cnt += red+1
            break
        # 外の並べ方
        cnt = j+1
        # 入れる赤の並べ方
        if insi>0:
            cnt *= cmb(red-j, insi-1)
        red_cnt += cnt
        print(f'i:{insi} j{j} cnt:{cnt} red:{red_cnt}')
    print(slice_cnt, red_cnt,slice_cnt * red_cnt)