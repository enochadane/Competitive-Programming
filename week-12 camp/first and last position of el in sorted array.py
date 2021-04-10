class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        starting = self.findBound(nums, target, True)
        if starting == -1:
            return [-1, -1]
        
        ending = self.findBound(nums, target, False)
        
        return [starting, ending]
    
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if isFirst:
                    if mid == low or nums[mid - 1] < target:
                        return mid
                    high = mid - 1
                else:
                    if mid == high or nums[mid + 1] > target:
                        return mid
                    low = mid + 1
                    
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
                