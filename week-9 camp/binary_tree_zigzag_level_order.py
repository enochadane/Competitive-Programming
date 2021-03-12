# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        queue = []
        output = []
        level = 0
        queue.append(root)
        while queue:
            temp = []
            level_len = len(queue)
            level += 1
            for i in range(level_len):
                node = queue.pop(0)
                if level % 2 == 0:
                    temp.insert(0, node.val)
                else:
                    temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(temp)
        return output