import sys
sys.setrecursionlimit(10**4)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Iterative solution

        # low = 0
        # high = len(nums) - 1
        # while low <= high:
        #     mid = (low + high) // 2
        #     if target == nums[mid]:
        #         return mid
        #     elif target > nums[mid]:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return -1

        # Recursive solution
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        return self.binarySearch(nums, 0, len(nums) - 1, target)
    
    def binarySearch(self, nums, low, high, target):
        mid = (low + high) // 2
        if low <= high:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binarySearch(nums, mid + 1, high, target)
            else:
                return self.binarySearch(nums, low, mid - 1, target)
        return -1