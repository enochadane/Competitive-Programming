# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root)
    def isLeaf(self, node: TreeNode)-> bool:
        return node.left == None and node.right == None
    
    def dfs(self, root: TreeNode) -> int:
        if self.isLeaf(root):
            return 1
        elif root.left and root.right:
            return min(self.dfs(root.left), self.dfs(root.right)) + 1
        elif root.left:
            return self.dfs(root.left) + 1
        else:
            return self.dfs(root.right) + 1
        
        
        
    
    
    
    # def bfs(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     queue = []
    #     queue.append(root)
    #     level = 1
    #     while len(queue):
    #         size = len(queue)
    #         for i in range(size):
    #             node = queue.pop(0)
    #             if self.isLeaf(node):
    #                 return level
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         level += 1
    #     return level