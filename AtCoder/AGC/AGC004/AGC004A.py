a,b,c = map(int, input().split())
def calc(x,y,z):
    print(((x -x//2) - x//2) * y * z)

if a%2==0:
    calc(a,b,c)
elif b%2==0:
    calc(b,a,c)
elif c%2==0:
    calc(c,a,b)
else:
    l = sorted([a,b,c])[::-1]
    calc(l[0], l[1], l[2])
