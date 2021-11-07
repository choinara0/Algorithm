import sys
from collections import deque

A, B = map(int ,sys.stdin.readline().split())
cnt, answer = 1, -1
q = deque()
q.append((A, cnt))

while q:
    num, c = q.popleft()

    if num == B:
        answer = c
        break

    if num*2 <= B:
        q.append((num*2, c+1))
    if int(str(num)+'1') <= B:
        q.append((int(str(num)+'1'), c+1))

print(answer)
