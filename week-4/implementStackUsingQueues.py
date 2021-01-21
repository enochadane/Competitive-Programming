class MyStack:

    def __init__(self):
        self.size = 0
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1
        

    def pop(self) -> int:
        top = self.queue.pop()
        self.size -= 1
        return top

    def top(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()