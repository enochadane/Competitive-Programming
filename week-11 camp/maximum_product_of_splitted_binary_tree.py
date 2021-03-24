# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        dp = {}
        max_, total = 0, self.sumAtNode(root, dp)
        return max([v * (total - v) for k,v in dp.items()]) % (10 ** 9  + 7)
    def sumAtNode(self, node: TreeNode, dp) -> int:        
        dp[node] = total = node.val + self.sumAtNode(node.left, dp) + self.sumAtNode(node.right, dp) if node else 0       
        return total
            