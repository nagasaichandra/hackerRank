#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    """
    Take two separate dictionaries to store the counts and frequencies of those counts
    """

    counts = dict()
    freqs = dict()
    out = []
    for i in queries:
        x = i[1]
        if x in counts:
            if i[0] == 1:
                counts[x] += 1
                freqs[counts[x] - 1] = freqs[counts[x] - 1] -1 if counts[x] - 1 in freqs else 0
                freqs[counts[x]] = freqs[counts[x]] + 1 if counts[x] in freqs else 1
            if i[0] == 2:
                if counts[x] > 0:
                    counts[x] -= 1
                    freqs[counts[x] + 1] = freqs[counts[x] + 1] -1 if counts[x] + 1 in freqs else 0
                    freqs[counts[x]] = freqs[counts[x]] + 1 if counts[x] in freqs else 1
        else:
            if i[0] == 1:
                counts[x] = 1
                freqs[1] = freqs[1] + 1 if 1 in freqs else 1
        if i[0] == 3:
            if i[1] in freqs and freqs[i[1]] > 0:
                out.append(1)
            else:
                out.append(0)            
            
                        
    return out
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
