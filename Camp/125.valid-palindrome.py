#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(l, r, s):
            if not self.isAlphaNumeric(s[l]):
                return
            if not self.isAlphaNumeric(s[r]):
                return
            if s[l].lower() != s[r].lower():
                return False
            return True
            helper(l + 1, r - 1, s)
        return helper(0, len(s) - 1, s)
    def isAlphaNumeric(self, c) -> bool:
        if (97 <= ord(c) <= 122) or (65 <= ord(c) <= 90) or (48 <= ord(c) <= 57):
            return True
        return False
# @lc code=end

