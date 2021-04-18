#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
def ret_count(s, k, p):
    # Takes the given arguments and a single pair, 
    # checks if there are matches for the pairs and returns 
    # the maximum of counts between matches of pair
    a = 0
    b = 0
    if p[0] == p[1] or p[0] == 0:
        for i in s:
            if i % k == p[0]:
                return 1
    if p[0] == p[1] or p[0] == 0:
        return 0
    for i in s:
        if i % k == p[0]:
            a += 1
        elif i % k == p[1]:
            b += 1
    return max(a, b)


def nonDivisibleSubset(k, s):
    # Write your code here
    rem_pairs = [(i, k-i) for i in range(0, (k//2)+1)]
    print(rem_pairs)
    count = 0
    for i in rem_pairs:
        count += ret_count(s, k, i)
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
