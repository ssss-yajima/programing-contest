q,h,s,d = map(int, input().split())
n = int(input())

q_2l = q*8
h_2l = h*4
s_2l = s*2
ans = (n - n%2) //2 * min(q_2l, h_2l, s_2l, d) 
ans += (n % 2) * min(q_2l, h_2l, s_2l) // 2 # 奇数リットルの場合
print(ans)
