#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefixSum = [cardPoints[0]]
        suffixSum = [None] * len(cardPoints)
        suffixSum[len(cardPoints) - 1] = cardPoints[len(cardPoints) - 1]
        for i in range(1, len(cardPoints)):
            prefixSum.append(prefixSum[i - 1] + cardPoints[i])
        for i in range(len(cardPoints) - 2, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + cardPoints[i]
        
        maxSum = max(prefixSum[k - 1], suffixSum[len(suffixSum) - k])
        r = len(suffixSum) - k + 1
        for l in range(k - 1):
            maxSum = max(maxSum, prefixSum[l] + suffixSum[r])
            r += 1
        return maxSum
# @lc code=end

