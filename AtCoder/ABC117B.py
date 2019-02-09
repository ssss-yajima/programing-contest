N = int(input())
ll = list(map(int,input().split()))

# print(N)
# print(ll)
print('Yes' if sum(ll) - 2 * max(ll) >0 else 'No')
