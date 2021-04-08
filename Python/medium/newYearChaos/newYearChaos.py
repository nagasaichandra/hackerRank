#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q = [p-1 for p in q]
    bribes = 0
    for i,p in enumerate(q):
        
        if p - i > 2:
            print('Too chaotic')
            return
    
        for j in range(max(p-1, 0), i):
            if q[j] > p:
                bribes += 1
    print(bribes)
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

# https://www.hackerrank.com/challenges/new-year-chaos/problem