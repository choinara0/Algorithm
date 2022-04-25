# bfs algorithm 이용
import sys
from collections import deque

def bfs(x):
    visited = [0] * (n+1)
    visited[x] = 1
    q = deque()
    q.append((x, 0))

    while q:
        x, cnt = q.popleft()

        for nx in graph[x]:
            if not visited[nx]:

                if nx == 1:
                    return cnt + 1

                q.append((nx, cnt+1))
                visited[nx] = 1

    return -1

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())

for _ in range(q):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
    result = [0]
    for i in range(2, n+1):
        result.append(bfs(i))

    print(' '.join(map(str, result)))