N = int(input())
ss = [input() for _ in range(N)]

contained = sum([s.count('AB') for s in ss])
B_hoge = sum([1 for s in ss if s[0]=='B'])
hoge_A = sum([1 for s in ss if s[-1]=='A'])
B_hoge_A = sum([1 for s in ss if s[0]=='B' and s[-1]=='A'])

B_hoge -= B_hoge_A
hoge_A -= B_hoge_A

ans = contained
if B_hoge_A==0:
    ans += min(B_hoge, hoge_A)
elif B_hoge + hoge_A > 0:
    ans += B_hoge_A + min(B_hoge, hoge_A)
else:
    ans += B_hoge_A -1
print(ans)
