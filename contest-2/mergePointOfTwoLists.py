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
    stack1 = []
    stack2 = []
    mergePoint = None
    while head1 is not None:
        stack1.append(head1)
        head1 = head1.next
    while head2 is not None:
        stack2.append(head2)
        head2 = head2.next
    for i in range(len(stack1)):
        if len(stack2) != 0 and stack1[len(stack1) -1 - i] == stack2[len(stack2) -1 - i]:
            mergePoint = stack1[len(stack1) - 1 - i].data
        else:
            break
    return mergePoint
            