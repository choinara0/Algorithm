import sys
from collections import deque
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
computerMatrix = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    computerMatrix[b].append(a)

def bfs(x, N):
    count = 0
    q = deque()
    q.append(x)
    visited = [0] * (N+1)
    visited[x] = 1

    while q:
        t = q.popleft()
        count += 1
        for c in computerMatrix[t]:
            if visited[c] == 0:
                visited[c] = 1
                q.append(c)
    return count

answer = 0
result = []
for i in range(1, N+1):
    if computerMatrix[i]:
        temp = bfs(i, N)
        if answer <= temp:
            if answer < temp:
                result = []
            answer = temp
            result.append(i)

print(*result)