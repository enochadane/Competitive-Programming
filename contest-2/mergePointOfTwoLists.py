# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    first = head1
    start = head2
    while first:
        while start:
            if first == start:
                return first.data
            start = start.next
        first = first.next
        start = head2
        
        
