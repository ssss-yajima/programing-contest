# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):

    score = 0
    for rook1_row_i, rook1_row in enumerate(A):
        for rook1_col_i, rook1_score in enumerate(rook1_row):
            rook2_max_score = 0
            for rook2_row_i, rook2_row in enumerate(A):
                if rook2_row_i == rook1_row_i:
                    continue
                for rook2_col_i, rook2_score in enumerate(rook2_row):
                    if (rook2_col_i == rook1_col_i):
                        continue
                    if rook2_max_score < rook2_score:
                        rook2_max_score = rook2_score
            print(rook1_score, rook2_max_score)
            if score < rook1_score + rook2_max_score:
                score = rook1_score + rook2_max_score
    return score


print(solution([[15, 1, 5], [16, 3, 8], [2, 6, 4]]))
