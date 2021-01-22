# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        addend = 0
        if not root:
            return 0
        if root.val >= low and root.val <= high:
            addend = root.val
            
        return addend + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
    
    
    
    
    # def addTwo(val, low, high):
    #     total = 0
    #     if val >= low and val <= high:
    #         return total += val
    