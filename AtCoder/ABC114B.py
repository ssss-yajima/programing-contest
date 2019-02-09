s = input()

ss=[]
for i in range(len(s)-2):
    ss.append(abs(int(s[i:i+3])-753))
# print(ss)
print(min(ss))