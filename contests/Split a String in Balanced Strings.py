class Solution:
    def balancedStringSplit(self, s: str) -> int:
        s = [char for char in s]
        counter = 0
        maxSplit = 0
        for i in range(len(s)):
            if s[i] == 'R':
                counter += 1
            elif s[i] == 'L':
                counter -= 1
            if counter == 0:
                maxSplit += 1
        return maxSplit