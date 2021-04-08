#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    strings = {}
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            key = frozenset(Counter(s[i:i+j]).items())
            strings[key] = strings.get(key, 0)+1
    count = 0
    for key in strings:
        count += strings[key] * (strings[key]-1)//2
    return count

    # https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
