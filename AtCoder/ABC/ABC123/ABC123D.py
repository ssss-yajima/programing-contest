import bisect

x,y,z,k = map(int, input().split())
aa = sorted(list(map(int, input().split())))[::-1]
bb = sorted(list(map(int, input().split())))[::-1]
cc = sorted(list(map(int, input().split())))[::-1]

ia,ib,ic = 0,0,0
aa_ = [aa[ia]]
bb_ = [bb[ib]]
cc_ = [cc[ic]]
while len(aa_)*len(bb_)*len(cc_) <=k:
    if ia<x and aa[ia] == min(aa[ia],bb[ib],cc[ic]):
        ia +=1
        aa_ += [aa[ia]]
    if ib<y and bb[ib] == min(aa[ia],bb[ib],cc[ic]):
        ib +=1
        bb_ += [bb[ib]]
    else:
        ic +=1
        cc_ += [cc[ic]]

score = []
for a in aa_:
    for b in bb_:
        for c in cc_:
            bisect.insort_right(score, a+b+c)
for s in score[::-1][:k]:
    print(s)