class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def depth(self):
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0
        Depth = leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1
        return Depth

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def depth(self):
        if self.root: self.root.depth()
        else: return 0

    def insert(self, value):
        self.currentNode = self.root
        while True:
            if value < self.currentNode.value:
                if self.currentNode.left != None:
                    self.currentNode = self.currentNode.left
                else:
                    self.currentNode.left = value
                    break
            else:
                if self.currentNode.right != None:
                    self.currentNode = self.currentNode.right
                else:
                    self.currentNode.right = value
                    break



head = Node(3)
bt = BinaryTree(head)
bt.insert(5)



