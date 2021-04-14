#!/bin/python3

# https://www.hackerrank.com/challenges/queens-attack-2/problem

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # Create a move for each direction
    moves = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1,-1], [0, -1]]
    # Use hash set as the lookup is O(1) instead of O(N) lookup in list
    obstacles = set(tuple(i) for i in obstacles)
    count = 0
    for move in moves:
        cur_r, cur_c = r_q, c_q
        while (cur_r + move[0] >= 1 and cur_r + move[0] <= n) and (cur_c + move[1] >= 1 and cur_c + move[1] <= n):
            cur_r += move[0]
            cur_c += move[1]
            if tuple([cur_r, cur_c]) in obstacles:
                break
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
