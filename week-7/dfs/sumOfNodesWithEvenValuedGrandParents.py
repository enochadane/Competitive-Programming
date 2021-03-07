
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = [0]
        return self.dfs(root, 1, total)
    def dfs(self, node: TreeNode, parent_val: int, total: list) -> int:
        if not node:
            return 0
        if node.left:
            if not parent_val % 2:
                total[0] += node.left.val
            self.dfs(node.left, node.val, total)
        if node.right:
            if not parent_val % 2:
                total[0] += node.right.val
            self.dfs(node.right, node.val, total)
        return total[0]