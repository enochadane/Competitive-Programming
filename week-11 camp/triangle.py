class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # top-down approach
        triangle_ = [[0 for i in row] for row in triangle]
        triangle_[0][0] = triangle[0][0]
        for i in range(1, len(triangle_)):
            for j in range(len(triangle_[i])):
                if j == 0:
                    triangle_[i][j] = triangle_[i-1][j] + triangle[i][j]
                elif j == len(triangle_[i]) - 1:
                    triangle_[i][j] = triangle_[i-1][j-1] + triangle[i][j]
                else:
                    triangle_[i][j] = min(triangle_[i-1][j-1], triangle_[i-1][j]) + triangle[i][j]
        return min(triangle_[len(triangle_) - 1])
        
        # bottom-up approach
        triangle_ = triangle[-1]
        for i in range(len(triangle) -2, -1, -1):
            for j in range(len(triangle[i])):
                triangle_[j] = min(triangle_[j], triangle_[j+1]) + triangle[i][j]
        return triangle_[0]