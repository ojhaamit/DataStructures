class Stack(object):
    def sortStack(self, stack):
        # print(stack)

        if len(stack) == 0:
            return stack
        
        top = stack.pop()
        # print(top)

        Stack().sortStack(stack)

        Stack().insertIntoSortedOrder(stack, top)

        return stack

    def insertIntoSortedOrder(self, stack, value):
        if len(stack) == 0 or stack[len(stack) - 1] <= value:
            stack.append(value)
            return
        
        top = stack.pop()
        Stack().insertIntoSortedOrder(stack, value)
        stack.append(top)

# Driver Code
input = [-5, 2, -2, 4, 3, 1]
print(Stack().sortStack(input))