# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
def check_valid(c):
    # given a counter c, goes through the values, and sees if all of them are equal.
    k = set(c.values())
    if 0 in k:
        k.remove(0)
    if len(k) == 1:
        return True
    
# Complete the isValid function below.
def isValid(s):
    c = Counter(s)  
    if check_valid(c):
        return 'YES'
    else:
        for i in c:
            c[i] -= 1
            if check_valid(c):
                return 'YES'
            c[i] += 1
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
