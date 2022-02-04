import sys
from collections import deque

N = int(sys.stdin.readline())
stepping_stone = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())
visited = [-1] * N

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0

    while q:
        x = q.popleft()
        for i in range(N):
            if (i-x)%stepping_stone[x] == 0 and visited[i] == -1:
                q.append(i)
                visited[i] = visited[x] + 1

                if i == b-1:
                    return visited[i]
    return -1

print(bfs(a-1))