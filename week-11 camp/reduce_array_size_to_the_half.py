from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = 1
        occurence = Counter(arr)
        
        lst = sorted([(k, v) for k, v in occurence.items()], key = lambda el: el[1], reverse = True)
        
        sum_ = 0
        i = 0
        while i < len(lst):
            sum_ += lst[i][1]
            if sum_ < (len(arr)/2):
                counter += 1
            i += 1
        return counter