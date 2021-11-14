import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
street = [[]*(N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    street[a].append(b)
answer = []
def bfs(x):
    q = deque()
    q.append((x, 0))
    visited = [0] * (N+1)
    visited[x] = 1

    while q:
        idx, cnt = q.popleft()
        if cnt == K:
            answer.append(idx)
            continue
        if street[idx]:
            for i in street[idx]:
                if not visited[i]:
                    q.append((i, cnt+1))
                    visited[i] = 1
    if answer:
        answer.sort()
        for i in answer:
            print(i)
    else:
        print(-1)
    return

bfs(X)
