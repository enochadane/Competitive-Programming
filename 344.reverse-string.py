#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s == '':
            return ''
        self.reverseString(s[1:] + [s[0]])
# @lc code=end

