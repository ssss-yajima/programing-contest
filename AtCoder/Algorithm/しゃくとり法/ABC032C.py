'''
ABC 032 C
https://atcoder.jp/contests/abc032/tasks/abc032_c
しゃくとり法で累積積
'''

N,K = map(int,input().split())
S = [int(input()) for _ in range(N)]

ri, li = 0,0
ans = 0
current = 1
# 0が含まれていれば無条件にOK
if S.count(0)>0:
    print(len(S))
else:
    while ri < N and li<=ri:
        if current <= K:
            # 右に進める
            current *= S[ri]
            ri += 1
        if current > K:
            # 左を縮める
            current /= S[li]
            li += 1
        ans =max(ans, ri-li)
        # print(f'li:{li} ri:{ri} mul:{current} {S[li:ri]} ans:{ans}')
    print(ans)
