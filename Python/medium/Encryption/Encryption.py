# https://www.hackerrank.com/challenges/encryption/problem?h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):

    s = s.strip(' ')
    f = math.floor(math.sqrt(len(s)))
    c = math.ceil(math.sqrt(len(s)))
    if f * c < len(s):
        f += 1
    table = []
    while len(s) > 0:
        table.append(list(s[:c]))
        s = s[c:]
    out = ['' for _ in range(c)]
    for i in range(len(table)):
        for j in range(len(table[i])):
            out[j] += table[i][j]            
    return ' '.join(out)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
