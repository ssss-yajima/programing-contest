n = int(input())
print('{:0=2}:{:0=2}:{:0=2}'.format(n//3600, n%3600//60, n%60))