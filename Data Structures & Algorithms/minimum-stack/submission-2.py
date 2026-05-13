class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print("appending to stack: ", val )
        # everytime we add, check min
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
            print("appending to min_stack: ", val )
        elif val <= self.min_stack[len(self.min_stack) - 1]:
            print("appending to min_stack: ", val )
            self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        print("popped: ", popped)
        if popped == self.min_stack[len(self.min_stack) - 1]:
            min_popped = self.min_stack.pop()
            print("poppedfrom min stack: ", min_popped)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        print("curr min_stack: ", self.min_stack)
        return self.min_stack[len(self.min_stack) - 1] 
