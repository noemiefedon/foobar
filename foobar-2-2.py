# -*- coding: utf-8 -*-

def my_func(x):
    "function to use for sorting elements"
    x = x.split('.')
    if len(x) == 2:
        return [int(x[0]), int(x[1]), 0, 2]
    if len(x) == 1:
        return [int(x[0]), 0, 0, 1]
    return [int(x[0]), int(x[1]), int(x[2]), 3]

def solution(l):
    "find the solution of the exercise 2 at level 2 of the foo.bar challenge"
    return sorted(l, key=my_func)

if __name__ == "__main__":
    l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
    print(solution(l))