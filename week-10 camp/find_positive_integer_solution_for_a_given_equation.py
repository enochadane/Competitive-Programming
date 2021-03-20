"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
        
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ret = []
        for y in range(1, 1001):
            x = self.findY(y, customfunction.f, z)
            
            ret.append([y, x])
            if (x == 1):
                break
#                 x_new = x
#                 y_new = y
#                 while y_new > 0 and x_new < 1001:
#                     if customfunction.f(x_new, y_new) == z:
#                         ret.append([x_new, y_new])
#                     x_new += 1
#                     y_new -= 1
                
#                 x_new = x - 1
#                 y_new = y + 1
#                 while x_new > 0 and y_new < 1001:
#                     if customfunction.f(x_new, y_new) == z:
#                         ret.append([x_new, y_new])
#                     x_new -= 1
#                     y_new += 1
#                 break
            
        return ret
    
    def findY(self, x, f, z):
        l = 1
        r = 1000
        while l <= r:
            mid = (l + r) // 2
            output = f(x, mid)
            if output == z:
                return mid
            if output > z:
                r = mid - 1
            else:
                l = mid + 1
        return 0                