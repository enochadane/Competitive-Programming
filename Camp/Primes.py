import math
n = int(input())
def primes(n):
    addend = n - 2
    root = math.ceil(math.sqrt(addend))
    isPrime = True
    for i in range(2, root + 1):
        if addend % i == 0:
            isPrime = False
    if isPrime and n > 3:
        print(2, addend)
    else:
        print(-1)

primes(n)