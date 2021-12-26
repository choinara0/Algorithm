import sys

doc = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()
cnt = 0
idx = 0
while len(doc) - idx >= len(word):
    if doc[idx:idx+len(word)] == word:
        cnt += 1
        idx += len(word)
    else:
        idx += 1
print(cnt)