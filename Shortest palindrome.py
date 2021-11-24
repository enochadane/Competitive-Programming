class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        pre = []
        foundPrefix = False
        for i in range(n - 1, -1, -1):
            r = i + 1
            l = i - 1
            mirror = 2
            while mirror > 0:
                while r < n and l >= 0:
                    if s[r] == s[l]:
                        r += 1
                        l -= 1
                    else:
                        break
                if l < 0:
                    break
                mirror -= 1
                r = i
                l = i - 1
            if l <= 0:
                while r < n:
                    pre.append(s[r])
                    r += 1
                break
        pre = reversed(pre)
        return ''.join(pre) + s
