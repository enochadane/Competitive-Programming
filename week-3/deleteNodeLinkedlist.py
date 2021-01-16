# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
myList = ListNode(4, 1)        

solution = Solution()
print(solution.deleteNode(4))