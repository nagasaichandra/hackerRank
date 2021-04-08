#!/bin/python3

import math
import os
import random
import re
import sys

def helper(arr, inds):
    i, j = inds
    x = 0
    for w in range(i-1, i+2):
        for y in range(j-1, j+2):
            x += arr[w][y]

    x -= arr[i][j-1]
    x -= arr[i][j+1]
    return x
    
    
# Complete the hourglassSum function below.
def hourglassSum(arr):
    #The arrays are 6x6
    indices = []
    for i in range(1, 5):
        for j in range(1, 5):
            indices.append((i, j))
    sums = []
    for ind in indices:
        sums.append(helper(arr, ind))
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
