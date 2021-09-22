class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_ = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                max_ = max(max_, counter)
                counter = 0
        return max(max_, counter)