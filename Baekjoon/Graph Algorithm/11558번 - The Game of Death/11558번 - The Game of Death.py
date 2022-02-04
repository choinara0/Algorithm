import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(x):
    q = deque()
    q.append((x, 0))
    visited[x] = 1
    while q:
        x, cnt = q.popleft()
        if x == N-1:
            return cnt
        if not visited[graph[x]]:
            q.append((graph[x], cnt+1))
            visited[graph[x]] = 1
    return 0

for _ in range(T):
    N = int(sys.stdin.readline())
    graph = [0] * N
    visited = [0] * N
    for i in range(N):
        A = int(sys.stdin.readline())
        graph[i] = A-1
    print(bfs(0))
