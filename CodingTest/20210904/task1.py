# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    if N % 2 == 1:
        return "a" * N
    else:
        return "a" * (N - 1) + "b"
