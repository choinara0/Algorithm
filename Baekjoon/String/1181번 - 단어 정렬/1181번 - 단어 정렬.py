import sys

N = int(sys.stdin.readline())
word_list = []

for _ in range(N):
    word_list.append(sys.stdin.readline().strip())
word_list = list(set(word_list))
word_list.sort(key=lambda x:(len(x), x))
print('\n'.join(word_list))