class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        seen = {1}
        while n:
            num = heapq.heappop(heap)
            if n == 1: return num
            for prime in primes:
                a = num * prime
                if a in seen: continue
                heapq.heappush(heap, a)
                seen.add(a)
            n -= 1
            