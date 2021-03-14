# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        left = right = False
        if not root:
            return 0
        if root.left:
            left = self.hasPathSum(root.left, targetSum - root.val)
        if root.right:
            right = self.hasPathSum(root.right, targetSum - root.val)
        
        if self.isLeaf(root) and root.val == targetSum:
            return True
        else:
            return left or right
        
        return total == targetSum
    def isLeaf(self, node: TreeNode) -> bool:
        return node.left == None and node.right == None