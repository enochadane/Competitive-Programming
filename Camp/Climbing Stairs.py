class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1]*(n+1)
        return self.dfs(n, memo)
    
    def dfs(self, n, memo):
        if n < 0:
            return 0
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        memo[n] = self.dfs(n - 1, memo) + self.dfs(n - 2, memo)
        
        return memo[n]