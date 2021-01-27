# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        sortedBST = self.traverse(root)
        print(sortedBST)
        
        minDiff = sortedBST[1] - sortedBST[0]
        for i in range(len(sortedBST) - 1):
            diff = sortedBST[i + 1] - sortedBST[i]
            if diff < minDiff:
                minDiff = diff
        return minDiff
    
    def traverse(self, root: TreeNode) -> List[int]:
        traversal = []
        if root:
            traversal += self.traverse(root.left)
            traversal += [root.val]
            traversal += self.traverse(root.right)
        
        return traversal