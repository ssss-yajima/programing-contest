s = 'abcabcabc'

target = 'c'
idx = [i for i,x in enumerate(s) if x==target]
print(idx)

# targetより右側を揃えるまで
print(len(s)-1 - idx[-1])

for i in range(len(idx)-1):
    idx[i+1] -= idx[i]
# targetより左を揃えるまで
print(idx)
