import sys

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        curr_node.data = string

    def searchPrefix(self, string):
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
        if curr_node.children:
            return False
        else:
            return True

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    trie = Trie()
    numList = []

    for j in range(N):
        num = sys.stdin.readline().strip()
        numList.append(num)
        trie.insert(num)

    check = True
    for num in numList:
        if not trie.searchPrefix(num):
            check = False
            break

    if check:
        print('YES')
    else:
        print('NO')