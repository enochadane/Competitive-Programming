class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        min_ = max(weights)
        max_ = sum(weights)
        capacity = 0
        
        while min_ <= max_:
            daysNeeded = 1
            currentWeight = 0
            mid = (min_ + max_) // 2
            
            for weight in weights:
                currentWeight += weight
                if currentWeight > mid:
                    daysNeeded += 1
                    currentWeight = weight
                
            if daysNeeded > D:
                min_ = mid + 1
            else:
                capacity = mid
                max_ = mid - 1
        return capacity
            
            