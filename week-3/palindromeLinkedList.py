# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    tail = None
    def isPalindrome(self, head):
        if head is None:
            return True
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        lst1 = head
        lst2 = self.reverseList(slow)
        while lst2 is not None:
            if lst1.val != lst2.val:
                return False
            lst1 = lst1.next
            lst2 = lst2.next
        return True
    
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
        

myList = ListNode(1, ListNode(1))        

solution = Solution()
print(solution.isPalindrome(myList))