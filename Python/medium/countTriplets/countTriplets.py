#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
"""
While going in a reverse direction, keep updating two dictionaries.. frequencies of each element, and frequencies of pairs (i, j) where a[j]//r==a[i]
for a target element in an iteration, if it has it's corresponding second and third parts in the "double" dictionary, we add that freq to count. 
We also update the double table and freq table for each target element.
Time complexity is essentially O(n) instead of O(n). Note that there are several search operations to dictionaries, they are all of O(1).
"""

def countTriplets(arr, r):
    count = 0
    freq = dict()
    double = dict()
    for i in range(len(arr)-1,-1, -1):
        first = arr[i]
        second = arr[i]*r
        third = arr[i]*r*r
        if (second, third) in double:
            count += double[(second, third)]
        if freq.get(second):
            if double.get((first, second)):
                double[(first, second)] += freq[second]
            else:
                double[(first, second)] = freq[second]
        if freq.get(first):
            freq[first] += 1
        else:
            freq[first] = 1
        
    return count

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
