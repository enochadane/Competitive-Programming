# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    def sumNumbers(self, root: TreeNode) -> int:
        
        return self.dfs(root, 0)
        
    def dfs(self, root: TreeNode, path: int) -> int:
        if root:
            if not root.left and not root.right:
                path = path*10 + root.val
                self.total += path
            self.dfs(root.left, path*10 + root.val)
            self.dfs(root.right, path*10 + root.val)
        return self.total
        