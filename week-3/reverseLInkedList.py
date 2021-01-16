# Definition for singly-linked list.

# iterative solution

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return
        prev = None
        currNode = head
        fast = currNode.next
        while fast is not None:
            currNode.next = prev
            prev = currNode
            currNode = fast
            fast = fast.next
        currNode.next = prev
        return currNode

# recursive solution

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    tail = None
    def reverseList(self, head):
        self.reverse(head)
        return self.tail
    def reverse(self, head):
        if head is None:
            return
        if head.next is None:
            self.tail = head
            return head
        myHead = self.reverse(head.next)
        myHead.next = head
        head.next = None
        
        return head


myList = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))        

solution = Solution()

print(solution.reverseList(myList))
        