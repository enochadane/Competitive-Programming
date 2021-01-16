class Solution(object):
    def hIndex(self, citations):
        indexH = 0
        bound = 0
        if citations:
            bound = max(citations)
        for i in range(bound + 1):
            countH = 0
            for j in range(len(citations)):
                if citations[j] >= i:
                    countH += 1
            if i <= countH:
                indexH = i
        return indexH
        