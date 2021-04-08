#!/bin/python3

import math
import os
import random
import re
import sys

def reverse(a):
    return [i for i in reversed(a)]

# Complete the candies function below.

# Create two empty lists. For first array, go left to right, initiate first 
# element as 1, if i-1 > i, then [i] is [i-1]+1, else [i] is 0. Do the same 
# once from right to left, and add the max of corresponding elements in both 
# arrays to count. This gets both the uptrends and downtrends in ratings. 
# Time Complexity is O(2XN) as the list is parsed twice
def candies(n, arr):
    up = []
    down = []
    up.append(1)
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            up.append(up[-1]+1)
        else:
            up.append(1)
    rev = reverse(arr)
    down.append(1)
    for i in range(1, len(rev)):
        if rev[i] > rev[i-1]:
            down.append(down[-1]+1)
        else:
            down.append(1)
    d = reverse(down)
    count = 0
    for j in range(len(d)):
        count += max(d[j], up[j])
    return count
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
