class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class MyLinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        if self.head is None:
            return -1
        currNode = self.head
        i = 0
        while i < index and currNode.next:
            currNode = currNode.next
            i += 1
        return currNode.val
        

    def addAtHead(self, val):
        NewNode = Node(val)
        if not self.head:
            self.head = NewNode
            self.tail = self.head
        else:
            NewNode.next = self.head
            self.head = NewNode
        self.size += 1

    def addAtTail(self, val):
        NewNode = Node(val)
        if not self.head:
            self.tail = self.head = NewNode
        self.tail.next = NewNode
        self.tail = NewNode
        self.size += 1

    def addAtIndex(self, index, val):
        NewNode = Node(val)
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        currNode = self.head
        prev = self.head
        i = 0
        while i < index:
            i += 1
            prev = currNode
            currNode = currNode.next
        prev.next = NewNode
        NewNode.next = currNode
        self.size += 1
        

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        currNode = self.head
        prev = self.head
        i = 0
        while i < index:
            i += 1
            prev = currNode
            currNode = currNode.next
        prev.next = currNode.next
        if index == self.size - 1:
            self.tail = prev
        self.size -= 1
            
  

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# test case
# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

myLinkedList = MyLinkedList()
print(myLinkedList.addAtHead(1))
currNode = myLinkedList.head
print(currNode.next)
while currNode:
    print("currNode", currNode.val)
    currNode = currNode.next
print(myLinkedList.addAtTail(3))
currNode = myLinkedList.head
print(currNode.next)
while currNode:
    print("currNode", currNode.val)
    currNode = currNode.next
print(myLinkedList.addAtIndex(1, 2))
currNode = myLinkedList.head
print(currNode.next)
while currNode:
    print("currNode", currNode.val)
    currNode = currNode.next
print(myLinkedList.get(1))
print(myLinkedList.deleteAtIndex(1))
print(myLinkedList.get(1))

print('*****************************************')
