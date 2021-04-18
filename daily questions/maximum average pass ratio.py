import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = [(-((a + 1)/(b + 1) - a/b), a, b) for a, b in classes]
        heapq.heapify(maxHeap)
        for _ in range(extraStudents):
            _, a, b = heappop(maxHeap)
            a += 1
            b += 1
            change = -((a + 1)/(b + 1) - a/b)
            heappush(maxHeap, (change, a, b))
        
        return sum(a/b for _, a, b in maxHeap) / len(classes)