#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    divBy3 = []
    divBy5 = []
    ans = ''
    for i in range(n + 1):
        if i % 3 == 0:
            divBy3.append(i)
        if i % 5 == 0:
            divBy5.append(i)
    isFound = False
    for num1 in divBy5:
        for num2 in divBy3:
            if num1 + num2 == n:
                isFound = True
                ans = '5' * num2
                ans += '3' * num1
                print(ans)
                break
        if isFound:
            break
    if not isFound:
        print(-1)
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
