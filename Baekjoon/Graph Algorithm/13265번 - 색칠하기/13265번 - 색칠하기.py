import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(x):
    global flag

    q = deque()
    q.append(x)
    visited[x] = 1
    color[x] = 1

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = 1
                if color[x] == 1:
                    color[nx] = 2
                else:
                    color[nx] = 1
                q.append(nx)
            if visited[nx] == 1 and color[x] == color[nx]:
                flag = 1
                return

    return

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] * (n+1) for i in range(n+1)]
    visited = [0] * (n+1)
    color = [0] * (n+1)
    flag = 0
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(len(color)):
        if color[i] == 0:
            bfs(i)

    if not flag:
        print('possible')
    else:
        print('impossible')