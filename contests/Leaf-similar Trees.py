# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafSequence1 = []
        leafSequence2 = []
        
        return self.dfs(root1, leafSequence1) == self.dfs(root2, leafSequence2)
    
    def dfs(self, root, leafSequence):
        if not root.left and not root.right:
            leafSequence.append(root.val)
        if root.left:
            self.dfs(root.left, leafSequence)
        if root.right:
            self.dfs(root.right, leafSequence)
        
        return leafSequence