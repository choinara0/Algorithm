import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
board = [list(map(str, sys.stdin.readline().strip())) for i in range(R)]
f_queue, j_queue = deque(), deque()
f_visited, j_visited = [[0]*C for i in range(R)], [[0]*C for i in range(R)]

def bfs():
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<R and 0<=ny<C and not f_visited[nx][ny]:
                if board[nx][ny] == '#':
                    continue
                f_queue.append((nx, ny))
                f_visited[nx][ny] = f_visited[x][y] + 1

    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                return j_visited[x][y] + 1

            if j_visited[nx][ny] != 0 or board[nx][ny] == '#' or (f_visited[nx][ny] != 0 and f_visited[nx][ny] <= j_visited[x][y] + 1):
                continue
            j_queue.append((nx, ny))
            j_visited[nx][ny] = j_visited[x][y] + 1

    return 'IMPOSSIBLE'

for i in range(R):
    for j in range(C):
        if board[i][j] == 'F':
            f_queue.append((i, j))
        elif board[i][j] == 'J':
            j_queue.append((i, j))

print(bfs())





