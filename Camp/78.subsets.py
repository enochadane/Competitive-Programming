#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [()]
        for n in nums:
            self.recurse([n], nums, ans)
        return list(set(ans))
    def recurse(self, arr, nums, ans):
        ans.append(tuple(sorted(arr)))
        for n in nums:
            if n not in arr:
                c_arr = arr[:]
                c_arr.append(n)
                # ans.append(sorted(c_arr))
                self.recurse(c_arr, nums, ans)
# @lc code=end

