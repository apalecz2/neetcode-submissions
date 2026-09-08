
# array?
# keep an array for the push pop top operations in O(1)
# then have a min heap for the getMin

# can use monotonic queue or something since every item could be popped back out and 
# any item could be the min again

# use a second array where at the index, the smallest element gets appended

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) <= 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
