import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
positions = list(map(int, sys.stdin.readline().split()))
dq = deque([i for i in range(1, N+1)])
count = 0

for position in positions:
    while True:
        if dq[0] == position:
            dq.popleft()
            break
        else:
            if dq.index(position) < len(dq) / 2:
                while dq[0] != position:
                    dq.append(dq.popleft())
                    count += 1
            else:
                while dq[0] != position:
                    dq.appendleft(dq.pop())
                    count += 1

print(count)