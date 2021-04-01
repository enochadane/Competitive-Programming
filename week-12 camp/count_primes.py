class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        primes = [i for i in range(n)]
        primes[0] = primes[1] = -1
        for i in range(2, len(primes)):
            if primes[i] == -1:
                continue
            markPoint = i * i
            while markPoint < n:
                primes[markPoint] = -1
                markPoint += i
            
        
        return len(primes) - primes.count(-1)