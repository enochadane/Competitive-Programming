# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        output = []
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
                
                level.append(node.val)
            output.append(level)
            
        return output