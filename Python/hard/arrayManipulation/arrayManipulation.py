#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/crush/problem
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for _ in range(n)]
    # arr_dict = dict(enumerate(arr))
    max_val = 0
    c = 0
    for q in queries:
        a = q[0]
        b = q[1]
        k = q[2]
        arr[a-1] += k
        if len(arr) > b:
            arr[b] -= k
    for i in arr:
        c += i
        if max_val < c:
            max_val = c
            
    return max_val
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
