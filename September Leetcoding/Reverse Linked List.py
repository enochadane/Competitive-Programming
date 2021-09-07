# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        lst = []
        node = head
        while node:
            lst.append(node)
            node = node.next
        for i in range(len(lst) - 1, 0, -1):
            lst[i].next = lst[i - 1]
        lst[0].next = None
        return lst[len(lst) - 1]