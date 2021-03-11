# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        output = []
        level = []
        level.append(root)
        while level:
            temp = []
            level_len = len(level)
            for i in range(len(level)):
                node = level.pop(0)
                temp.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            output.append(sum(temp)/len(temp))
            temp = []
        return output
            
            