class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        left, right = self.sortArray(nums[:len(nums)//2]), self.sortArray(nums[len(nums)//2:])
        
        return self.merge(left, right)
    def merge(self, left, right):
        merged = []
        i, j = 0, 0
        while len(left) > i and len(right) > j:
            if left[i] > right[j]:
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
        if len(left) == i:
            merged += right[j:]
        else:
            merged += left[i:]
        return merged