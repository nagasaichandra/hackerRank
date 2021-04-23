#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
import math
import os
import random
import re
import sys
from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a, b = max(a, b), min(a, b)
    c_a = Counter(a)
    c_b = Counter(b)
    count = 0
    for i in c_a:
        if c_a[i] > c_b[i]:
            print('a', c_a[i], c_b[i])
            count += c_a[i] - c_b[i]
            c_a[i] -= c_a[i] - c_b[i]
            print('out', c_a[i])
    for i in c_b:
        if c_b[i] > c_a[i]:
            print('b', c_b[i], c_a[i])
            count += c_b[i] - c_a[i]
            c_b[i] -= c_b[i] - c_a[i]
            print('out_b', c_b[i])
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
