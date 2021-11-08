import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
def bfs(f, s, g, u, d):
    q = deque()
    q.append((s, 0))
    visited = [0] * (f+1)
    while q:
        x, cnt = q.popleft()
        if x == g:
            print(cnt)
            return
        if x-d > 0 and not visited[x-d]:
            q.append((x-d, cnt+1))
            visited[x-d] = 1
        if x+u <= f and not visited[x+u]:
            q.append((x+u, cnt+1))
            visited[x+u] = 1
    print('use the stairs')
    return
bfs(F, S, G, U, D)