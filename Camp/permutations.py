class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

#second way
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for n in nums:
            self.recurse([n], nums, result)
        return result
    def recurse(self, arr, nums, result):
        if len(arr) == len(nums):
            result.append(arr)
        for n in nums:
            if n not in arr:
                c_arr = arr[:]
                c_arr.append(n)
                self.recurse(c_arr, nums, result)