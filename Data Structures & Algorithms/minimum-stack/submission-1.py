class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.mini = val
            self.stack.append(0)
        else:
            diff = val - self.mini
            self.mini = min(val, self.mini)
            self.stack.append(diff)

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff > 0:
            return
        else:
            self.mini = self.mini - diff

    def top(self) -> int:
        coded_value = self.stack[-1]
        if coded_value > 0:
            return self.mini + coded_value
        else:
            return self.mini

    def getMin(self) -> int:
        return self.mini
