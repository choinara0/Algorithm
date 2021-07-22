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

    def search(self, value):
        self.currentNode = self.root
        while self.currentNode:
            if self.currentNode.value == value:
                return True
            elif value < self.currentNode.value:
                self.currentNode = self.currentNode.left
            elif value > self.currentNode.value:
                self.currentNode = self.currentNode.right

        return False

    def delete(self, value):
        checkSearch = False # 삭제할 Node가 있는지 확인하기 위한 boolean 변수 선언
        self.currentNode, self.parent = self.root, self.root
        while self.currentNode: #삭제할 Node = self.currentNode, 삭제할 Node의 Parent Node = self.parent로 만드는 while문
            if self.currentNode.value == value:
                checkSearch = True
                break
            elif value < self.currentNode.value:
                self.parent = self.currentNode
                self.currentNode = self.currentNode.left
            elif value > self.currentNode.value:
                self.parent = self.currentNode
                self.currentNode = self.currentNode.right

        if checkSearch == False: #삭제할 노드가 없으면 False를 return
            return False
        #삭제할 Node가 Leaf Node인 경우
        if self.currentNode.left == None and self.currentNode.right == None:
            if value < self.parent.value:
                self.parent.left = None
            if value > self.parent.value:
                self.parent.right = None
        #삭제할 None가 Child Node를 1개 가지고 있을 경우
        elif self.currentNode.left != None and self.currentNode.right == None: #child Node가 currentNode의 왼쪽에 위치할 때
            if value < self.parent.value:
                self.parent.left = self.currentNode.left
            elif value > self.parent.value:
                self.parent.right = self.currentNode.left
        elif self.currentNode.left == None and self.currentNode.right != None: #child Node가 currentNode의 오른쪽 위치할 때
            if value < self.parent.value:
                self.parent.left = self.currentNode.right
            elif value > self.parent.value:
                self.parent.right = self.currentNode.right

        # 삭제할 Node가 Child Node를 2개 가지고 있을 경우
        elif self.currentNode.left != None and self.currentNode.right != None:
            if value < self.parent.value : #삭제할 Node가 삭제할 Node의 Parent보다 값이 작을 때
                self.changeNode = self.currentNode.right
                self.changeNodeParent = self.currentNode.right
                while self.changeNode.left != None:
                    self.changeNodeParent = self.changeNode
                    self.changeNode = self.changeNode.left
                if self.changeNode.right != None:
                    self.changeNodeParent.left = self.changeNode.right
                else:
                    self.changeNodeParent.left = None
                self.parent.left = self.changeNode
                self.changeNode.right = self.currentNode.right
                self.changeNode.left = self.currentNode.left

            elif value > self.parent.value : #삭제할 Node가 삭제할 Node의 parent보다 값이 클 때
                self.changeNode = self.currentNode.right
                self.changeNodeParent = self.currentNode.right
                while self.changeNode.lfet != None:
                    self.changeNodeParent = self.changeNode
                    self.changeNode = self.changeNode.left
                if self.changeNode.right != None:
                    self.changeNodeParent.left = self.changeNode.right
                else:
                    self.changeNodeParent.left = None
                self.parent.right = self.changeNode
                self.changeNode.right = self.currentNode.right
                self.changeNode.left = self.currentNode.left
        return True


head = Node(3)
bt = BinaryTree(head)
bt.insert(5)


