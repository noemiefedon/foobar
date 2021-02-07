# -*- coding: utf-8 -*-

def solution(x, y):
    "find the solution of the exercise 1 at level 2 of the foo.bar challenge"
    value = 1

    for ind_row in range(y):
        value += ind_row

    rate = y + 1

    for ind_col in range(x - 1):
        value += rate
        rate += 1

    return str(value)

if __name__ == "__main__":
    print(solution(3, 2))
