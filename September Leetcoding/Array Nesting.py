class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [0] * len(nums)
        max_ = 0
        for i in range(len(nums)):
            localMax = 0
            j = i
            while visited[j] == 0:
                localMax += 1
                visited[j] = 1
                j = nums[j]
            max_ = max(max_, localMax)
        
        return max_