# Special String Again
# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    l = []
    # fill the list l with tuples of consecutive characters and their counts
    cur = s[0]
    c = 1
    for i in range(1, n):
        if s[i] != cur:
            l.append((cur, c))
            cur = s[i]
            c = 1
        else:
            c += 1
    l.append((cur, c))    
    print(l)
    
    # Pass 2 : add the combinations of each substrings from l
    for i in l:
        count += int((i[1] * (i[1] + 1)) / 2)

    # pass 3: if a count in l is 1, then find min of it's neighbors
    for i in range(1, len(l)-1):
        if l[i][1] == 1 and l[i-1][0] == l[i+1][0]:
            count += min(l[i-1][1], l[i+1][1])
    return count

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
