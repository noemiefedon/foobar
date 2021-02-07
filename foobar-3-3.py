# -*- coding: utf-8 -*-

def solution(n):
    "find the solution of the exercise 2 at level 3 of the foo.bar challenge"
    n = int(n)
    count = 0
    while n > 1:
        if n % 2 == 0:             # last 2 elements of binary number: *0
            n = n // 2
        elif n == 3 or n % 4 == 1: # last 2 elements of binary number: 01
            n = n - 1
        else:                      # last 2 elements of binary number: 11 but not 3!
            n = n + 1
        count += 1
    return count

if __name__ == "__main__":
    print(solution('4'))
    print(solution(15))
