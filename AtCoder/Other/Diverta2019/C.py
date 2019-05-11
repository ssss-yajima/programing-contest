N = int(input())
ss = [input() for _ in range(N)]

contained = sum([s.count('AB') for s in ss])
B_hoge = sum([1 for s in ss if s[0]=='B'])
hoge_A = sum([1 for s in ss if s[-1]=='A'])
B_hoge_A = sum([1 for s in ss if s[0]=='B' and s[-1]=='A'])

B_hoge -= B_hoge_A
hoge_A -= B_hoge_A
gap = abs(B_hoge - hoge_A)
# 差がB_hoge_Aより大きい場合、可能な限り差を埋める
if gap >= B_hoge_A:
    print(contained + min(B_hoge,hoge_A) + B_hoge_A)
#　差がB_hoge_Aより小さい場合、差を埋めた残りでペアを作る
else:
    print(contained + max(B_hoge,hoge_A) + (B_hoge_A+1 - gap)//2)

# print('contained:',contained)
# print(B_hoge, hoge_A, B_hoge_A)
