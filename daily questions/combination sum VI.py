class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums, combs = sorted(nums), [1] + [0] * target
        for i in range(target + 1):
            for num in nums:
                if i < num: break
                if i == num:
                    combs[i] += 1
                if i > num:
                    combs[i] += combs[i - num]
        return combs[target]