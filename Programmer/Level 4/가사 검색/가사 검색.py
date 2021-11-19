class Node(object):
    def __init__(self, key):
        self.key = key
        self.data = 0
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(self)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            curr_node.data += 1
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data += 1


    def search(self, string):
        curr_node = self.head
        for char in string:
            if char == '?':
                break
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0

        return curr_node.data

def solution(words, queries):
    answer = []
    tries = {}
    reversed_tries = {}
    for w in words:
        if len(w) in tries:
            tries[len(w)].insert(w)
            reversed_tries[len(w)].insert(reversed(w))
        else:
            trie = Trie()
            reversed_trie = Trie()

            trie.insert(w)
            reversed_trie.insert(reversed(w))

            tries[len(w)] = trie
            reversed_tries[len(w)] = reversed_trie

    for q in queries:
        if len(q) in tries:
            if q[0] != '?':
                trie = tries[len(q)]
                answer.append(trie.search(q))
            else:
                trie = reversed_tries[len(q)]
                answer.append(trie.search(reversed(q)))
        else:
            answer.append(0)

    return answer

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]) #[3, 2, 4, 1, 0]
