#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u - 1].append((w, v))
        heap = [(0, k)]
        visited = {}
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            for w, v in graph[node - 1]:
                heapq.heappush(heap, (w + time, v))
            visited[node] = time
        return max(visited.values()) if len(visited) == n else - 1
# @lc code=end

