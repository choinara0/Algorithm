import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
line = [list(map(int, sys.stdin.readline().strip())) for _ in range(2)]
visited = [[0] * N for _ in range(2)]

def bfs():
    q = deque()
    q.append((0, 0))
    time = -1

    while q:
        for _ in range(len(q)):
            l, idx = q.popleft()
            if idx+1 >= N or idx + K >= N:
                return 1
            if line[l][idx+1] == 1 and not visited[l][idx+1]:
                q.append((l, idx+1))
                visited[l][idx+1] = 1
            if idx-1 > time+1 and line[l][idx-1] == 1 and not visited[l][idx-1]:
                q.append((l, idx-1))
                visited[l][idx-1] = 1
            if line[(l+1)%2][idx+K] == 1 and not visited[(l+1)%2][idx+K]:
                q.append(((l+1)%2, idx+K))
                visited[(l+1)%2][idx+K] = 1
        time += 1

    return 0

print(bfs())