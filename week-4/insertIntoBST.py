# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        NewNode = TreeNode(val)
        if not root:
            root = NewNode
        elif val < root.val:
            if not root.left:
                root.left = NewNode
            else:
                self.insertIntoBST(root.left, val)
        elif val > root.val:
            if not root.right:
                root.right = NewNode
            else:
                self.insertIntoBST(root.right, val)
        else:
            return
        return root