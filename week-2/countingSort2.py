#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    max = 0
    sortedArray = []
    for i in range(len(arr)):
        if(arr[i] > max):
            max = arr[i]
    countArray = [0] * (max + 1)
    for i in range(len(arr)):
        countArray[arr[i]] += 1
    for i in range(len(countArray)):
        for j in range (countArray[i]):
            sortedArray.append(i)
    print(sortedArray)
    return sortedArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
