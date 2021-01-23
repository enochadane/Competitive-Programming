# Enter your code here. Read input from STDIN. Print output to STDOUT

class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 


def height(root):
    depth = 0
    if not root:
        return 0
    if root.left or root.right:
        depth = 1
    return max(depth + height(root.left), depth + height(root.right))