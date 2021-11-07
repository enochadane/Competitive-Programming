from collections import defaultdict
def numOfPairs():
    t = int(input())
    for _ in range(t):
        nlr = list(map(int, input().split()))
        l = nlr[1]
        r = nlr[2]
        a = list(map(int, input().split()))
        d = defaultdict(int)
        for index, num in enumerate(a):
            d[num] = index
        count = 0
        for sum_ in range(l, r + 1):
            for i in range(len(a)):
                complement = sum_ - a[i]
                if complement in d and d[complement] > i:
                    count += 1
        print(count)

numOfPairs()