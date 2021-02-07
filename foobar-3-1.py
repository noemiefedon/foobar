# -*- coding: utf-8 -*-

import numpy as np

def solution(n):
    "find the solution of the exercise 1 at level 3 of the foo.bar challenge"

    record = np.zeros((n, n), int)
    # record[i1, i2] = number of stairs with i1 + 1 steps using i2 + 1 bricks
    record[0] = 1 # number of stairs with 1 step
    record[1, 2] = 1

    for ind_n in range(4, n + 1):

        ind_steps = 2

        while True:
            new = record[ind_steps - 2, ind_n - ind_steps - 1] \
            + record[ind_steps - 1, ind_n - ind_steps - 1]
            if new == 0:
                break
            else:
                record[ind_steps - 1, ind_n - 1] = new
                ind_steps += 1

    return sum(record[:, n - 1]) - 1

if __name__ == "__main__":
    print(solution(200))
