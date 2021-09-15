class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = [char for char in s]
        prefix = [0]*len(shifts)
        prefix[len(shifts) - 1] = shifts[len(shifts) - 1]
        for i in range(len(shifts) - 2, -1, -1):
            prefix[i] = prefix[i + 1] + shifts[i]
        for i in range(len(s)):
            s[i] = chr(((ord(s[i]) + prefix[i]) - ord('a')) % 26 + ord('a'))
        return ''.join(s)