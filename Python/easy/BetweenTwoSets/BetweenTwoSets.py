#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
from math import gcd
from functools import reduce

def make_gcd(arr):
    x = reduce(gcd, arr)
    return x

def lcm(a):
    lcm = 1
    for i in a:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm

def getTotalX(a, b):
    # Write your code here
    a = list(set(a))
    b = list(set(b))
    lcm_a = lcm(a)
    gcd_b = make_gcd(b)
    count = 0
    for i in range(max(a), min(b)+1):
        if i % lcm_a == 0 and gcd_b % i ==0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
