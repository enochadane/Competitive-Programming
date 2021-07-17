class Solution:
    def largestOddNumber(self, num: str) -> str:
        lst = [el for el in num]
        for i in range(len(lst) - 1, -1, -1):
            if int(lst[i]) % 2 == 1:
                return num[:i+1]
        
        return ""