import sys
from collections import deque

K = int(sys.stdin.readline())

for i in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for j in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    check = True

    for v in range(1, V+1):
        if visited[v] == 0:
            q.append(v)
            visited[v] = 1
            while q:
                x = q.popleft()
                for w in graph[x]:
                    if visited[w] == 0:
                        q.append(w)
                        visited[w] = -1 * visited[x]
                    elif visited[w] == visited[x]:
                        check = False

    print('YES' if check else 'NO')