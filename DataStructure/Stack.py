
class Stack:

    '''Initializing stack'''
    def __init__(self):
        self.stack = []

    '''Push element in stack'''
    def push(self,value):
        self.stack.append(value)

    '''To pop element out from stack'''
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise ValueError('stack is empty')

    '''To peek latest element in the stack'''
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            raise ValueError('stack is empty')

    '''To check whether stack is empty or not'''
    def isEmpty(self):
        return len(self.stack) == 0