class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroCells = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroCells.append((i, j))
        
        for cell in zeroCells:
            for i in range(len(matrix)):
                matrix[i][cell[1]] = 0
            for j in range(len(matrix[0])):
                matrix[cell[0]][j] = 0