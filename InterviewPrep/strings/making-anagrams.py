#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def genDict(temp):
    temp_dict = {}
    for i in temp:
        if i in temp_dict.keys():
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1
    return temp_dict

def genDictDiff(a_dict, b_dict):
    count = 0
    for key in a_dict.keys():
        if key not in b_dict.keys():
            count += a_dict[key]
        else:
            if a_dict[key] > b_dict[key]:
                count += a_dict[key] - b_dict[key]
    return count
    
def makeAnagram(a, b):
    # Write your code here
    a_dict = genDict(a)
    b_dict = genDict(b)
    deletions = 0
    a_del = genDictDiff(a_dict, b_dict)
    b_del = genDictDiff(b_dict, a_dict)
    return(a_del + b_del)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
