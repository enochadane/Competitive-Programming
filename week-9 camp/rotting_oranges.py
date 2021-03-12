class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        rottens = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten = (i, j)
                    rottens.append(rotten)
        toBeRotten = rottens
        while toBeRotten:
            size = len(toBeRotten)
            isRotten = False
            for i in range(size):
                node = toBeRotten.pop(0)
                bottom = (node[0] + 1, node[1])
                up = (node[0] - 1, node[1])
                right = (node[0], node[1] + 1)
                left = (node[0], node[1] - 1)
                if node[0] < m-1 and grid[bottom[0]][bottom[1]] == 1:
                    grid[bottom[0]][bottom[1]] = 2
                    toBeRotten.append(bottom)
                    isRotten = True
                if node[0] > 0 and grid[up[0]][up[1]] == 1:
                    grid[up[0]][up[1]] = 2
                    toBeRotten.append(up)
                    isRotten = True
                if node[1] < n-1 and grid[right[0]][right[1]] == 1:
                    grid[right[0]][right[1]] = 2
                    toBeRotten.append(right)
                    isRotten = True
                if node[1] > 0 and grid[left[0]][left[1]] == 1:
                    grid[left[0]][left[1]] = 2
                    toBeRotten.append(left)
                    isRotten = True
            if isRotten:
                minutes += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes
        
            