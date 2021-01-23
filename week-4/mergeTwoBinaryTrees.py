# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return
        elif t1 and t2:
            t1.val = t1.val + t2.val
        elif t1 is None and t2:
            t1 = TreeNode(0)
            t1.val = t1.val + t2.val
        else:
            t2 = TreeNode(0)
            t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1