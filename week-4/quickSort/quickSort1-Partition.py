#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    left, equal, right = [], [], []
    pivot = arr[0]
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el == pivot:
            equal.append(el)
        else:
            right.append(el)
    
    return left + equal + right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
