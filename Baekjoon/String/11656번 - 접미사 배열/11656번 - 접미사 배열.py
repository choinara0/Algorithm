import sys

word = list(map(str, sys.stdin.readline().strip()))
suffix_list = []

for i in range(len(word)):
    suffix_list.append(''.join(word[i:]))

suffix_list.sort()
print('\n'.join(suffix_list))