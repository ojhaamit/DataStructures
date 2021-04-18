class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self):
        spaces = " " * self.getLevel()
        print(spaces + self.data)
        # print(self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

def buildProductTree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("Dell"))
    laptop.addChild(TreeNode("ThinkPad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.addChild(TreeNode("iPhone"))
    cellphone.addChild(TreeNode("Google Pixel"))
    cellphone.addChild(TreeNode("Samsung Galaxy"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("Samsung"))
    tv.addChild(TreeNode("LG"))

    root.addChild(laptop)
    root.addChild(cellphone)
    root.addChild(tv)

    return root

if __name__ == '__main__':
    root = buildProductTree()
    print(root.printTree())
    # print(root.getLevel())