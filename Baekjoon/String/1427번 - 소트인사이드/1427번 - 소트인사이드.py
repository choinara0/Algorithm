import sys

word = sorted(list(map(int, sys.stdin.readline().strip())), reverse=True)
print(''.join(map(str, word)))
