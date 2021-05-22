class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        counter = 0
        maxLen = 0
        for rect in rectangles:
            localMax = min(rect[0], rect[1])
            if localMax > maxLen:
                maxLen = localMax
        
        for l, w in rectangles:
            if min(l, w) == maxLen:
                counter += 1
        
        return counter