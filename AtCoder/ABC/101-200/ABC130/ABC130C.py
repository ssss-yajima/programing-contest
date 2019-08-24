W,H,x,y = map(int,input().split())
AREA = 1.0*W*H

# 水平 or 垂直
if x==W/2 and y==H/2:
    print(AREA/2,1)
# 辺の上
else:
    print(AREA/2,0)
