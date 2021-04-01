from collections import defaultdict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        count = defaultdict(int)
        left = right = 0
        maxFruits = 1
        while right < len(tree):
            if len(count) <= 2:
                count[tree[right]] = right
            if len(count) > 2:
                min_ = len(tree) - 1
                for v in count.values():
                    min_ = min(min_, v)
                left = min_ + 1
                del count[tree[min_]]
                
            maxFruits = max(maxFruits, (right - left) + 1)
            
            right += 1
            
        return maxFruits
                