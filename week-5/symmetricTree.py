# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._isMirror(root.left, root.right)
        
    def _isMirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return root1 == root2
        if root1.val != root2.val:
            return False
        return self._isMirror(root1.left, root2.right) and self._isMirror(root1.right, root2.left)
            