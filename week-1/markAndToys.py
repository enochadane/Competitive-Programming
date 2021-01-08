#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    total = 0
    maxToys = 0
    sortedPrices = sorted(prices)
    i = 0
    while(i < len(sortedPrices) and total + sortedPrices[i] <= k):
        total += sortedPrices[i]
        maxToys += 1
        i += 1
    return maxToys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
