#!/bin/python3

import math
import os
import random
import re
import sys


def define_range(ran_start, ran_end, val): #Returns an updated range and a boolean
    # For a given value lets say 5 and a range lets say 7 to 13, function checks if 5 is outside the inclusive range and returns true, updated range; otherwise returns false, same range
    # 
    if val < ran_start:
        ran_start = val
        return (ran_start, ran_end, False, True)
    elif val > ran_end:
        ran_end = val
        return (ran_start, ran_end, True, False)
    else:
        return (ran_start, ran_end, False, False)

    # Complete the breakingRecords function below.
def breakingRecords(scores):
    ran_start = scores[0]
    ran_end = scores[0]
    times_w = []
    times_l = []
    for i in range(1, len(scores)):
        ran_start, ran_end, flag_w, flag_l = define_range(ran_start, ran_end, scores[i])
        times_w.append(flag_w)
        times_l.append(flag_l)
    c_w = sum(times_w)
    c_l = sum(times_l)
        
    return [c_w, c_l]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
