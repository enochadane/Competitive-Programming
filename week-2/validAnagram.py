class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        