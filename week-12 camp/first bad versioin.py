# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        low = 0
        high = n - 1
        start = n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                start = mid
                high = mid - 1
            else:
                low = mid + 1
        return start
        