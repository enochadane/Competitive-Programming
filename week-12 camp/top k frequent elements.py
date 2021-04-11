import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        frequency = [(-1 * v, k) for k, v in Counter(nums).items()]
        heapq.heapify(frequency)
        for i in range(k):
            output.append(heapq.heappop(frequency)[1])
            
        return output