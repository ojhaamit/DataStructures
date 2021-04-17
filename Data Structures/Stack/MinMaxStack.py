class MinMaxStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) -1]
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def push(self, number):
        self.stack.append(number)

    def getMin(self):
        minStack = self.stack[-1]
        for i in range(len(self.stack)):
             minStack = min(minStack, self.stack[i])
        return minStack

    def getMax(self):
        maxStack = float('-inf')
        for i in range(len(self.stack)):
            maxStack = max(maxStack, self.stack[i])
        return maxStack




# Driver Code
stack = MinMaxStack()
stack.push(5)
stack.push(7)
stack.push(2)
print(stack.peek())
print(stack.getMin())
print(stack.getMax())
stack.pop()
stack.pop()
print(stack.peek())
print(stack.getMin())
print(stack.getMax())
