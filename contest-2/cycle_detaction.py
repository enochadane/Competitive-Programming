# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if head is None or head.next is None:
        return 0
    currNode = head
    count = 0
    while currNode:
        if currNode.next == None:
            return 0
        currNode = currNode.next
        count += 1
        if count > 1000:
            break
    return 1