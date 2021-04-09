#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the repeatedString function below.
def repeatedString(s, n):
    temp = int(n/len(s))
    rem = n % len(s)
    cnt1 = Counter(s)
    count = cnt1['a']
    cnt2 = Counter(s[:rem])
    x = cnt2['a']
    return (count*temp)+x
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
