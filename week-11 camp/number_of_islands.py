class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    start = (y, x)
                    count += self.dfs(grid, x, y)
        return count
    
    def dfs(self, grid, x, y):
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
            return 0
        if grid[y][x] == '0':
            return 0
        
        grid[y][x] = '0'
        dirX = [1, -1, 0, 0]
        dirY = [0, 0, 1, -1]
        
        for i in range(len(dirX)):
            self.dfs(grid, x + dirX[i], y + dirY[i])
                
        return 1