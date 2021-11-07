`import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
computerMatrix = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    computerMatrix[b].append(a)

def bfs(x):
    cnt = 1
    visited = [0 for i in range(N+1)]
    visited[x] = 1
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for k in computerMatrix[x]:
            if not visited[k]:
                q.append(k)
                visited[k] = 1
                cnt += 1

    return cnt

maxCnt = 0
result = []
for i in range(1, N+1):
    cnt = bfs(i)
    if cnt >= maxCnt:
        maxCnt = cnt
    result.append([i, cnt])

for i, cnt in result:
    if cnt == maxCnt:
        print(i, end=' ')`