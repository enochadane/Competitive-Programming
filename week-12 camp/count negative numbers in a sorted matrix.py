class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            if row[0] < 0:
                count += len(row)
                continue
            if row[len(row) - 1] >= 0:
                continue
            count += self.binSearch(row)
        
        return count
    
    def binSearch(self, nums) -> int:
        count = 0
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < 0:
                count = len(nums) - mid
                high = mid - 1
            else:
                low = mid + 1
        return count