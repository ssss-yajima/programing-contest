N = int(input())
A = [int(input()) for _ in range(N)]
sorted_A = sorted(A)

for a in A:
    if sorted_A[-1] == a:
        print(sorted_A[-2])
    else:
        print(sorted_A[-1])