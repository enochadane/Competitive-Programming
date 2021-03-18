# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        visited = set()
        new_G = []
        startNode = head
        while startNode:
            if startNode.val in G:
                new_G.append(startNode.val)
            startNode = startNode.next
        for num in new_G:
            if num in visited:
                continue
            else:
                node = self.findNode(head, num)
            while node and node.val in new_G:
                visited.add(node.val)
                node = node.next
            count +=1
            
        return count
        
    def findNode(self, node: ListNode, val: int) -> ListNode:
        while node:
            if node.val == val:
                return node
            node = node.next
            
            