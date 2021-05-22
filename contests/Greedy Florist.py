#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c = sorted(c, reverse=True)
    print(c)
    totalCost = 0
    previous = 0
    for i in range(len(c)):
        totalCost += (previous + 1) * c[i]
        if (i + 1) % k == 0:
            previous += 1
    return totalCost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()