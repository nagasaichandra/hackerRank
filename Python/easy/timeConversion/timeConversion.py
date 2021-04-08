#!/bin/python3

import os
import sys
# https://www.hackerrank.com/challenges/time-conversion/problem
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if "12" == s[:2] and "AM" in s[-2:]:
        return "00"+s[2:-2]
    if "AM" in s or s[:2]=="12":
        return s[:-2]
    elif "PM" in s:
        return str(int(s[:2])+12)+s[2:-2]
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
