# Two pointers approach

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, len(nums) - 1
                while k < l:
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum_ > target or (l < len(nums) - 1 and nums[l] == nums[l + 1]):
                        l -= 1
                    elif sum_ < target or (k > j + 1 and nums[k] == nums[k - 1]):
                        k += 1
                    else:
                        output.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
        return output