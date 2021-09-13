import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

matrix = []
for i in range(N):
    matrix.append(list(map(int, list(sys.stdin.readline().strip()))))
visited = [[[0]*2 for i in range(M)] for i in range(N)]
visited[0][0][1] = 1

def bfs():
    q = deque()
    q.append((0, 0, 1))
    while(q):
        x, y, check = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][check]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if (0<=new_x<N and 0<=new_y<M):
                if matrix[new_x][new_y] == 1 and check == 1:
                    visited[new_x][new_y][0] = visited[x][y][1] + 1
                    q.append((new_x, new_y, 0))
                if matrix[new_x][new_y] == 0 and visited[new_x][new_y][check] == 0:
                    visited[new_x][new_y][check] = visited[x][y][check] + 1
                    q.append((new_x, new_y, check))
    return -1

print(bfs())