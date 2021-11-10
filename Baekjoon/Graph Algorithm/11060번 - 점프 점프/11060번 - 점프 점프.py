import sys
from collections import deque

N = int(sys.stdin.readline())
maze = list(map(int, sys.stdin.readline().split()))
visited = [0] * (N)
visited[0]= 1

def bfs(x, cnt):
    q = deque()
    q.append((x, cnt))
    while q:
        idx, count = q.popleft()
        if idx == N-1:
            return count
        for i in range(1, maze[idx] + 1):
            nextIdx = idx + i
            if nextIdx < N and maze[nextIdx] > 0 and not visited[nextIdx]:
                visited[nextIdx] = 1
                q.append((nextIdx, count+1))

    return -1

print(bfs(0, 0))