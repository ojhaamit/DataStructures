class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryTreeNode(data)

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()
        return elements

    
    def preOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        # elements.append(self.data)
        if self.right:
            elements += self.right.preOrderTraversal()
        return elements

    
    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        
        if self.right:
            elements += self.right.postOrderTraversal()
        
        elements.append(self.data)
        return elements

    def search(self, data):
        if self.data == data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def findMin(self):
        if self.left is None:
            return self.data
        
        return self.left.findMin()

    def findMax(self):
        if self.right is None:
            return self.data
        
        return self.right.findMax()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            minValue = self.right.findMin()
            self.data = minValue
            self.right = self.right.delete(minValue)

        return self

def buildTree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbersTree = buildTree(numbers)
    print(numbersTree.inOrderTraversal())
    print(numbersTree.preOrderTraversal())
    print(numbersTree.postOrderTraversal())
    find = numbersTree.search(0)
    print(find)
    minElement = numbersTree.findMin()
    print(minElement)
    maxElement = numbersTree.findMax()
    print(maxElement)
    numbersTree.delete(20)
    print(numbersTree.inOrderTraversal())