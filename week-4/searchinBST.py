# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        #Iterative

        # while root:
        #     if root.val == val:
        #         return root
        #     elif root.val < val and root.right:
        #         root = root.right
        #     elif root.val > val and root.left:
        #         root = root.left
        #     else:
        #         return

        #Recursive

        if val == root.val:
            return root
        elif val > root.val and root.right:
            root = root.right
            return self.searchBST(root, val)
        elif val < root.val and root.left:
            root = root.left
            return self.searchBST(root, val)
        else:
            return
        return