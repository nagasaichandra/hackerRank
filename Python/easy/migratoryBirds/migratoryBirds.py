#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count = Counter(arr)
    print(count)
    max_val = max(count.values())
    max_keys = [k for k, v in count.items() if v == max_val]
    return min(max_keys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
