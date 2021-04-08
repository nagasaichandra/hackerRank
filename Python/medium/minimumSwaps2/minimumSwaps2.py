#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] == i+1:
            i += 1
            continue
        count += 1
        key = arr[arr[i]-1]
        arr[arr[i]-1] = arr[i]
        arr[i] = key
        
             
    return count
            
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

# https://www.hackerrank.com/challenges/minimum-swaps-2/problem