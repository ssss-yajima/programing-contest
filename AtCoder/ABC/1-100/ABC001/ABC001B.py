m = int(input())/1000
ans=0
if m<0.1:
    ans=0
elif 0.1 <= m <= 5:
    ans = m*10
elif 6 <= m <= 30:
    ans = m+50
elif 35 <= m <= 70:
    ans = (m-30)//5 + 80
else:
    ans = 89
print('{:0>2}'.format(int(ans)))
