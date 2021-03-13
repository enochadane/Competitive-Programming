#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    left_diagonal = []
    right_diagonal = []
    left_total = 0
    right_total = 0
    for i in range(n):
        left_diagonal.append((i, i))
        left_total += arr[i][i]
        right_total += arr[i][n - 1 - i]
    # for i in range(n):
    #     right_diagonal.append((i, (n - 1) - i))
    # for i in range(len(left_diagonal)):
    #     left_total += arr[left_diagonal[i]]
    print(left_total, right_total)
    return abs(left_total - right_total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
