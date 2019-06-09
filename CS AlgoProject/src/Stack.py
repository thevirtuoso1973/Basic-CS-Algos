class Stack: # OOP implementation of a stack
    def __init__(self):
        self.stack = [] # uses a list
        self.head = -1 # initialized to empty

    def push(self, val):
        self.stack.append(val) # adds to end
        self.head += 1 # increments pointer

    def pop(self):
        if self.head == -1: # checks if empty
            return None
        self.head -= 1 # decrements pointer (since item will be removed)
        return self.stack.pop(self.head) # removes and returns

    def max(self):
        if self.head == -1: # checks if empty
            return None
        return self.stack[self.head] # returns the appropriate val
