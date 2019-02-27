ss = input()
sn = (ss.count('S')>0) - (ss.count('N')>0)
ew = (ss.count('W')>0) - (ss.count('E')>0)
print('Yes' if  sn==0 and ew==0 else 'No')