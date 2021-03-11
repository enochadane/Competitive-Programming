class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        temp = 0
        maxlength = 0
        totalCost = 0
        difference = []
        firstPointer = 0
        secondPointer = 1
        for i in range(len(s)):
            difference.append(abs(ord(s[i]) - ord(t[i])))
        for i in range(len(difference)):
            if totalCost + difference[firstPointer] <= maxCost:
                maxlength += 1
                totalCost += difference[firstPointer]
                while secondPointer <= len(difference) - 1:
                    if totalCost + difference[secondPointer] <= maxCost:
                        maxlength += 1
                        totalCost += difference[secondPointer]
                    secondPointer += 1
            firstPointer += 1
            if maxlength > temp:
                temp = maxlength
            maxlength = 0
            totalCost = 0
            
        return temp
            
            