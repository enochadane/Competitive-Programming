class MyQueue:

    def __init__(self):
        self.size = 0
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        self.size += 1

    def pop(self) -> int:
        if len(self.stack) == 0:
            return
        first = self.stack.pop()
        self.size -= 1
        return first

    def peek(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1]
        

    def empty(self) -> bool:
        
        if len(self.stack) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()