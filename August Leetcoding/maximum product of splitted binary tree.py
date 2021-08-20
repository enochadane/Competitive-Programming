# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            subTreeSum = dfs(root.left) + dfs(root.right) + root.val
            self.ans = max(self.ans, subTreeSum * (self.totalSum - subTreeSum))
            return subTreeSum
        self.ans, self.totalSum = 0, 0
        self.totalSum = dfs(root)
        dfs(root)
        return self.ans % (10 **9 + 7)