
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.bfs(root)
    def isLeaf(self, node: TreeNode)-> bool:
        return node.left == None and node.right == None
    
    def dfs(self, root: TreeNode):
        if not root:
            return
        
        
    
    
    
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