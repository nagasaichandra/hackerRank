# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#
# The number of balls in each container should match the number of balls in each type in some manner.
def organizingContainers(container):
    # Write your code here
    no_of_balls_in_each_container = [sum(i) for i in container]
    no_of_balls_in_each_type = [0 for _ in range(len(container[0]))]
    
    for i in range(len(container)):
        for j in range(len(container[0])):
            no_of_balls_in_each_type[j] += container[i][j]
    a = sorted(no_of_balls_in_each_container)
    b = sorted(no_of_balls_in_each_type)
    if a==b:
        return 'Possible'
    else:
        return 'Impossible'
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
