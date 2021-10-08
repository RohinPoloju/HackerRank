#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    sa = sorted(list(set(a)))
    sb = sorted(list(set(b)))
    sc = sorted(list(set(c)))
    ai, bi, ci = 0 , 0, 0
    result = 0
    while bi < len(sb):
        while ai < len(sa) and sa[ai] <= sb[bi]:
            ai += 1
        
        while ci < len(sc) and sc[ci] <= sb[bi]:
            ci += 1
        
        result += ai * ci
        bi += 1
    return result
        
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
