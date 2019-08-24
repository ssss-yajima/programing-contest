aa = [int(input()) for _ in range(5)]
k = int(input())
if max(aa) - min(aa) > k:
    print(':(')
else:
    print('Yay!')