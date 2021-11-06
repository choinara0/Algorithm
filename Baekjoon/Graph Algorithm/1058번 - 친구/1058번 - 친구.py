import sys
from collections import deque
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
friendMatrix = [[0]*N for i in range(N)]
for i in range(N):
    temp = list(map(str, sys.stdin.readline()))
    for j in range(len(temp)):
        if temp[j] == 'Y':
            friendMatrix[i][j] = 1

def dfs(i, N):
    visited = [0] * N
    visited[i] = 1
    q = deque()
    q.append((i, 0))
    count = 0

    while q:
        i, c = q.popleft()
        if c >= 2:
            continue
        for k in range(N):
            if visited[k] == 0 and friendMatrix[i][k] == 1:
                count += 1
                visited[k] = 1
                q.append((k, c+1))

    return count

answer = 0
for i in range(N):
    answer = max(answer, dfs(i, N))

print(answer)
