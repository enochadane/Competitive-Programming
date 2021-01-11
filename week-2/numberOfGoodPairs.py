class Solution(object):
    def numIdenticalPairs(self, nums):
        countGoodPairs = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[i] == nums [j]:
                    countGoodPairs += 1
        
        return countGoodPairs
        