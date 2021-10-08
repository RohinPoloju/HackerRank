#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#
def genDict(s):
    s_dict = {}
    for i in s:
        if i in s_dict.keys():
            s_dict[i] += 1
        else:
            s_dict[i] = 1
    return(s_dict)
def check(m_dict, n_dict):
    for k in n_dict.keys():
        if k not in m_dict.keys():
            return "No"
        elif m_dict[k] < n_dict[k]:
            return "No"
    return "Yes"
def checkMagazine(magazine, note):
    # Write your code here
    
    m_dict = genDict(magazine)
    n_dict = genDict(note)
    print(check(m_dict, n_dict))
                
    
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
