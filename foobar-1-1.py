# -*- coding: utf-8 -*-

def solution(s):
    "find the solution of the exercise 1 at level 1 of the foo.bar challenge"
    n = len(s)

    for ind in range(1, n + 1):

        if n % ind:
            continue

        n_repeat = n // ind
        first_set = s[:ind]

        found_solution = True
        for ind2 in range(n_repeat - 1):
            other_set = s[(ind2+1)*ind:(ind2+2)*ind]

            if not first_set  == other_set:
                found_solution = False
                break
        if found_solution:
            return n // ind

    return 0

if __name__ == "__main__":

    #s='abcabcabcabc'
    #s ='aaaa'
    s='abccbaabccba'
    print(solution(s))