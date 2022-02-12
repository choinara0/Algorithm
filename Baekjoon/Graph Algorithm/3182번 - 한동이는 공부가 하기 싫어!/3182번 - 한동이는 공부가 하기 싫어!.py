import sys
from collections import deque

N = int(sys.stdin.readline())
answer = []
graph = [[]*(N+1) for i in range(N+1)]
for i in range(1, N+1):
    a = int(sys.stdin.readline())
    graph[i].append(a)

def bfs(x):
    visited = [0] * (N+1)
    visited[x] = 1
    q = deque()
    q.append((x, 0))

    while q:
        x, cnt = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append((i, cnt+1))
                visited[i] = 1

    return cnt

for i in range(1, N+1):
    answer.append(bfs(i))

print(answer.index(max(answer))+1)