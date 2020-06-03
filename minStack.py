class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        if not len(self.mins):
            self.mins.append(x)
        elif x <= self.mins[-1]:
            self.mins.append(x)
        
        self.stack.append(x)

    def pop(self) -> None:
        if self.top() == self.mins[-1]:
            self.mins.pop()

        self.stack.pop()

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.mins) > 0:
            return self.mins[-1]

obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
obj.getMin()
obj.pop()
print(obj.getMin())