#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    icecream_b = {}
    for i in range(len(cost)):
        if cost[i] not in icecream_b.keys():
            icecream_b[cost[i]] = (i+1, money - cost[i])
        else:
            if money == 2 * cost[i]:
                print(icecream_b[cost[i]][0], i+1)
                break
    if len(icecream_b.keys()) == len(set(cost)):
        for k in icecream_b.keys():
            if icecream_b[k][1] in icecream_b.keys() and icecream_b[k][0] != icecream_b[icecream_b[k][1]][0] :
                print(icecream_b[k][0], icecream_b[icecream_b[k][1]][0])
                break
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
