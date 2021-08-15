class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        allCells = []
        for i in range(rows):
            for j in range(cols):
                allCells.append([i, j, self.getDistance(rCenter, cCenter, i, j)])
        allCells = sorted(allCells, key = lambda cell: cell[2])
        ans = []
        for i, j, _ in allCells:
            ans.append([i, j])
            
        return ans
    
    def getDistance(self, r1, c1, r2, c2) -> int:
        rowD = r1 - r2 if r1 > r2 else r2 - r1
        colD = c1 - c2 if c1 > c2 else c2 - c1
        
        return rowD + colD