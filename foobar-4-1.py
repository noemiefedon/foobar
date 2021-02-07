# -*- coding: utf-8 -*-

from collections import deque

def add_source_and_sink(entrances, exits, path):
    "add a common source and a common sink"

    # at most 50 rooms -> at most 2 500 edges
    # at most 2 000 000 bunnies
    n_rooms = len(path[0])

    # Step 1 ------------------------------------------------------------------
    # create a new entrance connected to all other entrances with max capacity
    # -------------------------------------------------------------------------
    maxint = 2000000 * 50
    first_row = [maxint if i in entrances else 0 for i in range(n_rooms)]
    path.insert(0, first_row)
    for i in range(n_rooms + 1):
        path[i].insert(0, 0)

    # Step 2 ------------------------------------------------------------------
    # create a new exit connected to all other exitss with max capacity
    # -------------------------------------------------------------------------
    path[0].append(0)
    path.append([0]*(n_rooms + 2))

    for i in range(n_rooms):
        if i in exits:
            path[i + 1].append(maxint)
        else:
            path[i + 1].append(0)
    return 0


def calculate_adjacency_dic(path):
    "compute the dictionary of the room adjacencies"
    n_rooms = len(path[0])
    adjacency = dict()
    for i in range(n_rooms):
        for j in range(n_rooms):
            if path[i][j] != 0:
                # one way
                if i not in adjacency.keys():
                    adjacency[i] = [j]
                elif j not in adjacency[i]:
                    adjacency[i].append(j)

                # the other way
                if j not in adjacency.keys():
                    adjacency[j] = [i]
                elif i not in adjacency[j]:
                    adjacency[j].append(i)

    return adjacency


def find_augmenting_path(path, adjacency, n_rooms):
    """
    Find an angmenting path if possible by a breadth-first serach, update the
    residual capacity matrix,and return the flow increment.

    If there is no augmenting path, return and IndexError Exception.
    """

    parents = [-1] * n_rooms
    parents[0] = -2
    # parents = -2: there is no parent, source node
    # parents = -1: node not visited

    queue = deque()
    queue.appendleft((0, 2000000 * 50)) # add from left, remove from right

    while True:

        current_node, current_node_flow = queue.pop()

        for next_node in adjacency[current_node]:

            if parents[next_node] == -1: # if next_node is not visited

                next_flow = min(current_node_flow,
                                path[current_node][next_node])
                if next_flow > 0:
                    queue.appendleft((next_node, next_flow))
                    parents[next_node] = current_node

                    if next_node == n_rooms -1: # sink

                        # update capacities
                        while True:
                            path[current_node][next_node] -= next_flow
                            path[next_node][current_node] += next_flow

                            next_node = current_node
                            current_node = parents[current_node]

                            if current_node == -2: # source
                                break

                        return next_flow


def solution(entrances, exits, path):
    """
    find the solution of the exercise 1 at level 4 of the foo.bar challenge

    return max flow capacity using Edmonds-Karp Algorithm
    """

    add_source_and_sink(entrances, exits, path)
    # path is now the residual matrix

    # dictionary of the adjacencies assuming undirected graph
    adjacency = calculate_adjacency_dic(path)

    n_rooms = len(path[0])

    flow = 0

    while True:
        try:
            next_flow = find_augmenting_path(path, adjacency, n_rooms)
        except:
            break
        flow += next_flow

    return flow

if __name__ == "__main__":

    print(solution([0, 1],
                   [4, 5],
                   [[0, 0, 4, 6, 0, 0],
                    [0, 0, 5, 2, 0, 0],
                    [0, 0, 0, 0, 4, 4],
                    [0, 0, 0, 0, 6, 6],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]), 16)

    print(solution([0],
                   [3],
                   [[0, 7, 0, 0],
                    [0, 0, 6, 0],
                    [0, 0, 0, 8],
                    [9, 0, 0, 0]]), 6)
