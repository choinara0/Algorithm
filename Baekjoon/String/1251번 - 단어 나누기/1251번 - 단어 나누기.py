import sys

word = list(map(str, sys.stdin.readline().strip()))
divided_word_list = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        word1 = word[:i][::-1]
        word2 = word[i:j][::-1]
        word3 = word[j:][::-1]
        word_temp = word1 + word2 + word3
        divided_word_list.append(''.join(word_temp))

divided_word_list.sort()
print(divided_word_list[0])
