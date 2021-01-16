class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        counter = 0
        if s == "":
            return 0
        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
            elif s[i] == ")":
                counter -= 1
            depth = max(depth, counter)
        return depth
            