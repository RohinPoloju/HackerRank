#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
sys.setrecursionlimit(10000)

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

#def in_order_traversal():
def create_binary_tree(root, indexes):
    q = deque([root])
    for x,y in indexes:
        temp = q.popleft()

        if x != -1:
            temp.left = Node(x)
            q.append(temp.left)

        if y != -1:
            temp.right = Node(y)
            q.append(temp.right)
    
    return(root)
    
    
def swap_subtree_at_a_depth(root, depth, level, l):
    if root:
        if level % depth == 0:
            root.left, root.right = root.right, root.left
        
        swap_subtree_at_a_depth(root.left, depth, level+1, l)
        l.append(root.data)
        swap_subtree_at_a_depth(root.right, depth, level+1, l)
        
    return l

    
def swapNodes(indexes, queries):
    root = Node(1)
    root = create_binary_tree(root, indexes)
    
    result = []

    for depth in queries:
        l = []
        result.append(swap_subtree_at_a_depth(root, depth, 1, l))
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
