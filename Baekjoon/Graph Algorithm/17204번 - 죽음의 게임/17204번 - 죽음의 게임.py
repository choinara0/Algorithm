import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
numList = [int(sys.stdin.readline()) for i in range(N)]
visited = [0 for i in range(N)]

def bfs():
    q = deque()
    q.append((0))
    while q:
        node = q.popleft()
        value = numList[node]
        if visited[value] == 0 and node != value:
            q.append((value))
            visited[value] = visited[node] + 1
            if value == K:
                return

bfs()
print(visited[K] if visited[K] else -1)