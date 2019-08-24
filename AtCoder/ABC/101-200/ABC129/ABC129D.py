H,W = map(int, input().split())
S = [list(input()) for _ in range(H)]

w_score = [[0]*W for _ in range(H)]
h_score = [[0]*W for _ in range(H)]

begin = -1
streak = 1
for hi in range(H):
    for wi in range(W):
        if begin == -1 and S[hi][wi]=='.':
            begin = wi
        elif begin != -1 and S[hi][wi] == '.':
            streak += 1
        if wi ==W-1 or(begin != -1 and S[hi][wi]=='#'):
            if wi == W-1 and S[hi][wi]=='.':
                w_score[hi][wi]=streak
            for i in range(W)[begin:wi]:
                w_score[hi][i] = streak
            streak = 1
            begin = -1

# for s in w_score:
#     print(s)
# print('-'*10)

begin = -1
streak = 1
for wi in range(W):
    for hi in range(H):
        if begin == -1 and S[hi][wi]=='.':
            begin = hi
        elif begin != -1 and S[hi][wi] == '.':
            streak += 1
        if hi ==H-1 or(begin != -1 and S[hi][wi]=='#'):
            if hi == H-1 and S[hi][wi]=='.':
                h_score[hi][wi]= streak
            for i in range(H)[begin:hi]:
                h_score[i][wi] = streak
            streak = 1
            begin = -1

# for s in h_score:
#     print(s)
# print('-'*10)

ans = 0
score = [[0]*W for _ in range(H)]
for hi in range(H):
    for wi in range(W):
        w =w_score[hi][wi] 
        h= h_score[hi][wi] 
        score_ = w+h
        score_ += -1 if w>0 and h>0 else 0
        ans = max(ans,score_)
        score[hi][wi] = score_
        
# for s in score:
#     print(s)

print(ans)