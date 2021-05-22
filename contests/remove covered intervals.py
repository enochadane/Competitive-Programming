class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = set()
        for i in range(len(intervals) - 1):
            for j in range(i + 1, len(intervals)):
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    covered.add(j)
                elif intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    covered.add(i)
                    break
                else:
                    continue
        
        return len(intervals) - len(covered)