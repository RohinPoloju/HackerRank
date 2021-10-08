#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    high = max(machines) * goal
    low = 1
    while low < high:
        mid = (low + high) // 2
        itm = 0
        for i in range(len(machines)):
            itm += mid // machines[i]
        
        if itm < goal:
            low = mid + 1
        else:
            high = mid
    return high

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
