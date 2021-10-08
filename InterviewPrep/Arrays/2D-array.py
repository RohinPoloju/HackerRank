#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    result = []
    # for k in range(0,4):
    #     for i in range(0,4):
    #         sum_val = 0
    #         for j in range(0,3):
    #             sum_val += arr[k][i+j] + arr[2+k][i+j]
    #             sum_val += arr[1+k][1+i]
    #     result.append(sum_val)
    # return(max(result))
    a = arr
    for i in range(4):
        for j in range(4):
            sum_val = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
            result.append(sum_val)
    return(max(result))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
