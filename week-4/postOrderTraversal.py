# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        if root:
            traversal += self.postorderTraversal(root.left)
            traversal += self.postorderTraversal(root.right)
            traversal.append(root.val)
            
        return traversal