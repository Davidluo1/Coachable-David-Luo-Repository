class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        self.stack.append([val, min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None

    # def __init__(self):
    #     self.stack = []
    #     self.min = []

    # def push(self, val: int) -> None:
    #     if not self.min or val <= self.min[-1]:
    #         self.min.append(val)
    #     self.stack.append(val)

    # def pop(self) -> None:
    #     if self.stack[-1] <= self.min[-1]:
    #         self.min.pop()
    #     self.stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()