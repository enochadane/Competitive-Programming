class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for pre, nxt in relations:
            graph[pre - 1].append(nxt - 1)
            indegree[nxt - 1] += 1
        heap = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                heap.append((time[i], i))
        heapq.heapify(heap)
        totalTime = 0
        while heap:
            month, curr = heapq.heappop(heap)
            for node in graph[curr]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    heapq.heappush(heap, (month + time[node], node))
            totalTime = max(totalTime, month)
        
        return totalTime