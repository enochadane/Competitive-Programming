class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        #count consecutive zeros
        #check if the zeros are b/n 1s or not
        #if the zeros are b/n 1s: append no. of zeros - 1 in to my list else: append no. of zeros in to my list
        maxDist = 0
        first = -1
        last = -1
        count = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                count +=1
                if i == len(seats) -1:
                    maxDist = max(count, maxDist)
            else:
                if first != -1:
                    last = i
                first = i
                if first == last and count != 1:
                    if count %2 == 0:
                        count = count // 2
                    else:
                        count = (count + 1) // 2
                maxDist = max(count, maxDist)
                count = 0
                
            
        return maxDist