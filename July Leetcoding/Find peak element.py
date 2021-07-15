# Iterative binary search solution

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while(low < high):
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low


# Recursive binary search solution

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        return self.binSearch(low, high, nums)
    
    def binSearch(self, low, high, nums):
        if low == high:
            return low
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            return self.binSearch(low, mid, nums)
        return self.binSearch(mid + 1, high, nums)
        
# Linear O(n) solution

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1