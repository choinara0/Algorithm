import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque(enumerate(map(int, sys.stdin.readline().split())))
answer = []

while q:
    idx, num = q.popleft()
    answer.append(idx+1)
    if num > 0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)

print(' '.join(map(str, answer)))
