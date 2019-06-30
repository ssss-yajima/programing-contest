cc = [list(input().split()) for _ in range(4)]

for c in cc[::-1]:
    print(' '.join(c[::-1]))
print()