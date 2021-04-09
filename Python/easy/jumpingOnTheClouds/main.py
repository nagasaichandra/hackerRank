#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    key = 0
    count = 0
    while key < len(c)-1:
        if key == len(c) - 2:
            return count + 1
        if c[key+2]==1:
            key += 1
        else:
            key += 2
        count += 1        
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
