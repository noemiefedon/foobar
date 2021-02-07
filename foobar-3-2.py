# -*- coding: utf-8 -*-

def solution(liste):
    "find the solution of the exercise 2 at level 3 of the foo.bar challenge"

    dic_pos = dict()
    dic_a_divides_b = dict()
    dic_b_divides_a = dict()

    for ind, elem in enumerate(liste):

        if elem in dic_pos:
            # value already scanned
            dic_pos[elem].add(ind)
        else:
            # value not already scanned
            dic_pos[elem] = {ind}

            for bef in dic_pos:
                # bef divides elem
                if elem % bef == 0:
                    if bef in dic_a_divides_b:
                        dic_a_divides_b[bef].add(elem)
                    else:
                        dic_a_divides_b[bef] = {elem}

                    if elem in dic_b_divides_a:
                        dic_b_divides_a[elem].add(bef)
                    else:
                        dic_b_divides_a[elem] = {bef}

                # elem divides bef
                if bef % elem == 0:
                    if elem in dic_a_divides_b:
                        dic_a_divides_b[elem].add(bef)
                    else:
                        dic_a_divides_b[elem] = {bef}

                    if bef in dic_b_divides_a:
                        dic_b_divides_a[bef].add(elem)
                    else:
                        dic_b_divides_a[bef] = {elem}

    mysum = 0

    for ind, elem in enumerate(liste):
        if not elem in dic_a_divides_b or not elem in dic_b_divides_a:
            continue
        pos_before = []
        for elem2 in dic_b_divides_a[elem]:
            for pos in dic_pos[elem2]:
                if pos < ind:
                    pos_before.append(pos)
        if len(pos_before) == 0:
            continue
        pos_after = []
        for elem2 in dic_a_divides_b[elem]:
            for pos in dic_pos[elem2]:
                if pos > ind:
                    pos_after.append(pos)
        mysum += (len(pos_after) * len(pos_before))

    return mysum

if __name__ == "__main__":
    print(solution([1, 1, 1]))
    print(solution([1, 2, 3, 4, 5, 6]))
