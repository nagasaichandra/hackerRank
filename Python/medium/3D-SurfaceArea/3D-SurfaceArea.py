#!/bin/python3

# https://www.hackerrank.com/challenges/3d-surface-area/problem

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    height = len(A)
    width = len(A[0])
    # Initialize a table with size H+2 and W+2, and initialize such that boundaries are 0s and A is on the inside
    table = [[0 for _ in range(width+2)] for _ in range(height+2)]
    for i in range(1, len(table)-1):
        for j in range(1, len(table[0])-1):
            table[i][j] = A[i-1][j-1]
    area = 2 * height * width
    for i in range(1, len(table)-1):
        for j in range(1, len(table[0]) - 1):
            area += max(0, table[i][j] - table[i][j-1])
            area += max(0, table[i][j] - table[i-1][j])
            area += max(0, table[i][j] - table[i][j+1])
            area += max(0, table[i][j] - table[i+1][j])
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
