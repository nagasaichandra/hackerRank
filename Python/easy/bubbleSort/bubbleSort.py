#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

# Array is sorted in 3 swaps.  
# First Element: 1  
# Last Element: 6  

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if (a[j] > a[j + 1]):
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                count += 1
    print('Array is sorted in {} swaps.'.format(count))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
