# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):

    digit_dict = {}
    for a in A:
        digit_sum = sum(list(map(int, str(a))))
        if digit_sum in digit_dict:
            # keep maximum 2 numbers
            # item[0] < item[1]
            items = digit_dict[digit_sum]
            if len(items) < 2:
                items.append(a)
                items.sort()
            else:
                # if a > larget item, replace smaller item
                if items[1] < a:
                    items[0] = a
                    items.sort()
        else:
            digit_dict[digit_sum] = [a]
    # calc answer
    ans = -1
    for digit_pair in digit_dict.values():
        if len(digit_pair) < 2:
            continue
        sum_of_two = digit_pair[0] + digit_pair[1]
        if ans < sum_of_two:
            ans = sum_of_two
    return ans


print(solution([51, 17, 71, 42, 99]))
