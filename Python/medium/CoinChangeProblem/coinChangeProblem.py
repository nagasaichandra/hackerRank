#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    # Given n = target sum
    # c = array of denominations
    # First lets create a table of dimenssions c+1*n+1
    table = [[0 for _ in range(n+1)]for _ in range(len(c)+1)]
    for i in range(len(c)+1):
        table[i][0] = 1
        
    for i in range(1, len(c)+1):
        for j in range(1, n+1):

            top = table[i-1][j]
        
            if j-c[i-1] >= 0:
                left = table[i][j - c[i-1]]
            else:
                left = 0
            table[i][j] = top + left
    
    return table[len(c)][n]
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
