from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0]*k
        activeMinutes = defaultdict(set)
        for Id, time in logs:
            activeMinutes[Id].add(time)
        
        for activeMinute in activeMinutes.values():
            n = len(activeMinute)
            if n <= k:
                ans[n - 1] += 1
        
        return ans