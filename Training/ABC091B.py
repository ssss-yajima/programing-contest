n = int(input())
ss =[input() for _ in range(n)]
m=int(input())
tt = [input() for _ in range(m)]

sss=list(set(ss))
nums = [0] * (len(sss)+1)
for i,s in enumerate(sss):
    nums[i]=ss.count(s) - tt.count(s)
print(max(nums))