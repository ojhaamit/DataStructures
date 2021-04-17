class Node(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None
    
    def push(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if not self.head:
            return None
        else:
            popped = self.head.value
            self.head = self.head.next
            return popped

    def __repr__(self):
        res = self.head
        stack = ""
        while res != None:
            stack += str(res.value)
            res = res.next
        return stack

x = Stack()
x.push(1)
x.push(2)
print(x)
print(x.pop())
print(x)
print(x.pop())
print(x)