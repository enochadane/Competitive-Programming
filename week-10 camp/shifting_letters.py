class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        s = [el for el in S]
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i+1]
        for i in range(len(s)):
            s[i] = chr((((ord(s[i]) - 97) + (shifts[i] % 26)) % 26) + 97)
        return ''.join(s)
    