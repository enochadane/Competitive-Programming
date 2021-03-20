class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)
        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i -1] + nums[i -1]
            rightSum[len(nums) - i -1] = rightSum[len(nums) -i] + nums[len(nums) -i]
            
        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i
        return -1