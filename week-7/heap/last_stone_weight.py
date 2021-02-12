import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * el for el in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            weight1 = -1 * heapq.heappop(stones)
            weight2 = -1 * heapq.heappop(stones)
            if weight1 != weight2:
                diff = self.getDifference(weight1, weight2)
                heapq.heappush(stones, -1 * diff)
        if not stones:
            return 0
        return -1 * stones[0]
            
    def getDifference(self, num1: int, num2: int):
        if num1 > num2:
            return num1 - num2
        return num2 - num1