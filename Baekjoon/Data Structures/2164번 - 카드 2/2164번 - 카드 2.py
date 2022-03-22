import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([i for i in range(1, N+1)])
count = 0

while len(q)>1:

    if count%2 == 0:
        q.popleft()
        count += 1
    elif count%2 == 1:
        q.rotate(-1)
        count += 1

print(q[0])