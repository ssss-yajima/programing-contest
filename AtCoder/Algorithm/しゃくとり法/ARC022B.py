'''
https://atcoder.jp/contests/arc022/tasks/arc022_2
'''
N = int(input())
A = list(map(int, input().split()))

li,ri = 0,0
ans = 0
cnt = 0
exists = [0 for _ in range(10**6)] # 10**5だとOut Of Rnage
while ri < N and li <= ri:
    # お菓子が未登場なら右に進め、お菓子出現フラグON
    if not exists[A[ri]]:
        exists[A[ri]] = 1
        ri +=1
        cnt += 1
    else:
    # お菓子が登場済なら左を縮め、お菓子出現フラグOFF
        exists[A[li]] = 0
        li += 1
        cnt -= 1
    ans = max(ans, cnt)
    # print(f'li:{li} ri:{ri} {A[li:ri]} ans:{ans}')
print(ans)
