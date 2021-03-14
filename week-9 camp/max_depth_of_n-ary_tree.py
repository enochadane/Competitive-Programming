"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        count = 0
        if not root:
            return 0
        if self.isLeaf(root):
            return 1
        for child in root.children:
            depth = 0
            depth += self.maxDepth(child)
            count = max(count, depth)
        return count +1
    
    def isLeaf(self, node: 'Node') -> bool:
        return node.children == None
    