class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s = [str for str in s]
        t = [str for str in t]
        d = {}
        for i, char in enumerate(s):
            if char in d:
                if d[char] != t[i]:
                    return False
            elif t[i] in d.values():
                return False
            else:
                d[char] = t[i]
        return True