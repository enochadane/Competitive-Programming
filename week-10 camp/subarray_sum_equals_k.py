class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        occurence = {0:1}
        sum_ = 0
        for num in nums:
            sum_ += num
            if sum_ - k in occurence:
                count += occurence[sum_ - k]
            if sum_ in occurence:
                occurence[sum_] += 1
            else:
                occurence[sum_] = 1
        return count