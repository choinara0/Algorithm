import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
friendMatrix = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    friendMatrix[a].append(b)
    friendMatrix[b].append(a)

def bfs(x):
    count = 0
    visited = [0] * (N+1)
    visited[x] = 1
    q = deque()
    q.append((x, 0))

    while q:
        x, cnt = q.popleft()
        for i in friendMatrix[x]:
            if not visited[i] and cnt < 2:
                visited[i] = 1
                q.append((i, cnt+1))
                count += 1
    return count

print(bfs(1))
