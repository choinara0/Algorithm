import sys
from collections import deque

N = int(sys.stdin.readline())
result = [i for i in range(10)]

def dfs():
    q = deque()
    for i in range(1, 10):
        q.append((i, str(i)))
    while q:
        if len(result) == N+1:
            break
        x, y = q.popleft()
        if x != 0:
            for i in range(x):
                temp = y + str(i)
                q.append((i, temp))
                result.append(temp)

if N >=10:
    dfs()
if len(result) > N:
    print(result[N])
else:
    print(-1)