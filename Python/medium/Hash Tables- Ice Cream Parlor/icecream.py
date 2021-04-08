#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    '''
    Don't use the traditional approach of taking IDs or indices as 
    keys and struggle finding desired elements in values of dictionary.
    Instead use the costs as keys, so looking for their presence is way easier.'''
    cost_id = dict()
    for i, price in enumerate(cost):
        if (money - price) in cost_id:
            print(f"{cost_id[money - price]+1} {i+1}")
            break
        if price in cost_id:
            continue
        else:
            cost_id[price] = i

        
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
