import sys
import math
# sys.setrecursionlimit(2 * (10 ** 5))
def updateFiles():
    t = int(input())
    for _ in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        hour = 0
        updated = 1
        while updated < k:
            updated *= 2
        hour += math.log(updated,2)
        hour += updated / k

        print(math.ceil(hour))

        # def recurse(num, k, hour):
        #     if num <= 1:
        #         return 0
        #     if k >= num / 2:
        #         num = num / 2
        #         hour += 1
        #     elif k < num / 2:
        #         num //= k
        #         hour += num
        #     return 1 + recurse(num, k, hour)
        # hour = recurse(n, k, 0)
        # print(hour)
        
updateFiles()

