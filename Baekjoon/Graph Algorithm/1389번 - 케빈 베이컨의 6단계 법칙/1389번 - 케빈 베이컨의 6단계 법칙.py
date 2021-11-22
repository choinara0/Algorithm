import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
friendGraph = [[] for i in range(N+1)]
result = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    friendGraph[a].append(b)
    friendGraph[b].append(a)

def bfs(x):
    global N
    cntMatrix = [0] * (N+1)
    visited = [0] * (N+1)
    visited[x] = 1
    q = deque()
    q.append(x)
    count = 0
    while q:
        x = q.popleft()
        for i in friendGraph[x]:
            if not visited[i]:
                cntMatrix[i] = cntMatrix[x] + 1
                q.append(i)
                visited[i] = 1

    return sum(cntMatrix)

for i in range(1, N+1):
    result.append(bfs(i))
print(result.index(min(result))+1)
