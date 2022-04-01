import sys
from itertools import permutations

def dfs(depth, string):
    global answer

    if depth == len(word):
        answer += 1
        return

    for char in char_set:
        idx = ord(char) - ord('a')
        if alphabet[idx] == 0:
            continue
        if string and string[-1] == char:
            continue

        alphabet[idx] -= 1
        dfs(depth+1, string+char)
        alphabet[idx] += 1

word = list(map(str, sys.stdin.readline().strip()))
alphabet = [0] * 26
answer = 0
char_set = set()

for char in word:
    idx = ord(char) - ord('a')
    alphabet[idx] = alphabet[idx] + 1
    char_set.add(char)

dfs(0, '')
print(answer)