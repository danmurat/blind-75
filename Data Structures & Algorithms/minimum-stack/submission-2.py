class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        #self.minimum: int = 2^31
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        end: int = len(self.stack) - 1
        min_end: int = len(self.min_stack) - 1
        if self.min_stack[min_end] == self.stack[end]: # need to pop both
            del self.min_stack[min_end]

        del self.stack[end]

    def top(self) -> int:
        end: int = len(self.stack) - 1
        return self.stack[end]
        
    def getMin(self) -> int:
        #print(f"length = {len(self.min_stack)}")
        return self.min_stack[len(self.min_stack) - 1]
        
