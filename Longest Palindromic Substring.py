class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i in range(len(s)):
            l = i - 1
            mirror = 2
            while mirror > 0:
                r = i + 1
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        l -= 1
                        r += 1
                    else:
                        break
                if r - l - 1 > len(ans):
                    ans = s[l+1:r]
                mirror -= 1
                l = i
        return ans
