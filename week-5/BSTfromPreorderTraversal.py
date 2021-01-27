# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder), 1):
            self.insert(root, preorder[i])
        
        return root
    
    def insert(self, root: TreeNode, val: int):
        NewNode = TreeNode(val)
        if not root:
            root = NewNode
        elif root.val < val:
            if not root.right:
                root.right = NewNode
            else:
                self.insert(root.right, val)
        elif root.val > val:
            if not root.left:
                root.left = NewNode
            else:
                self.insert(root.left, val)
        else:
            return