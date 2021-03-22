class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSum = []
        for r in range(len(self.matrix)):
            row = self.matrix[r]
            prefixRow = [0]
            for i in range(len(row)):
                prefixRow.append(prefixRow[i] + row[i])
            self.prefixSum.append(prefixRow)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = 0
        for i in range(row1, row2 + 1):
            row = self.prefixSum[i]
            sum_ += row[col2 + 1] - row[col1]
            
        return sum_


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(row1,col1,row2,col2)