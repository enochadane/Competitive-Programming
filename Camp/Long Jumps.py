from typing import DefaultDict
import sys
sys.setrecursionlimit(4 * ( 10 ** 5) + 3)

def longJumps():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        memo = DefaultDict(int)
        dp = [0] * len(arr)
        dp[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            nxt = i + arr[i]
            if nxt < n:
                dp[i] = arr[i] + dp[nxt]
            else:
                dp[i] = arr[i]
        
        print(max(dp))

        # def recurse(index, n):
        #     if index >= n:
        #         return 0
        #     if index in memo:
        #         return memo[index]
        #     memo[index] = arr[index] + recurse(index + arr[index], n)
        #     return memo[index]
        # for ind in range(n):
        #     recurse(ind, n)
        # print(max(memo.values()))

longJumps()