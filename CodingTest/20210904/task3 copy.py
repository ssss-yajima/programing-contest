# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):

    cells = []

    for row_i, row in enumerate(A):
        for col_i, score in enumerate(row):
            cells.append([score, row_i, col_i])

    cells.sort()
    score = 0
    for i, rook1 in enumerate(cells):
        for rook2 in cells[i::]:
            if (rook2[1] == rook1[1] | rook2[2] == rook1[2]):
                continue
            tmp = rook1[0] + rook2[0]
            if score < tmp:
                score = tmp
            continue

    return score


print(solution([[15, 1, 5], [16, 3, 8], [2, 6, 4]]))
