class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n = n + 1
        while not self.isBalanced(n):
            n += 1
        return n
    def isBalanced(self, num: int) -> bool:
        num = str(num)
        num = list(num)
        counter = Counter(num)
        for k in counter:
            if int(k) != counter[k]:
                return False
        return True