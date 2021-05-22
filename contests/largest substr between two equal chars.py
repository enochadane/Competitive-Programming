class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = 0
        end = len(s) - 1
        noEqual = True
        for i in range(len(s)):
            start = s[i]
            last = s[end]
            for j in range(end, i, -1):
                if s[j] == start:
                    noEqual = False
                    localCount = j - i - 1
                    count = localCount if localCount > count else count
            
                    
        return -1 if noEqual else count