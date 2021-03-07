# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.result = None
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        kth = self.inOrderTraversal(root, k)
        return kth.val
    def inOrderTraversal(self, node: TreeNode, k: int) -> TreeNode:
        if node is None:
            return
        self.inOrderTraversal(node.left, k)
        
        self.count += 1
        if self.count == k:
            self.result = node
            
        self.inOrderTraversal(node.right, k)
        
        return self.result
        