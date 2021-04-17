class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return []

    def __repr__(self):
        return str(self.stack)

x = Stack() # Creating object of Stack class
x.push(1) # Pushing 1 to stack
x.push(2)  # Pushing 2 to stack
print(x) # arr = [1,2]
x.pop() # Deleting the last element from the stack.
print(x) # arr = [1]
print(x.pop()) # 1
print(x.pop()) # None(because stack is already empty)
