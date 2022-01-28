import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
Hx, Hy = map(int, sys.stdin.readline().split())
Ex, Ey = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for i in range(2)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[0][x][y] = 1
    answer = 0

    while q:
        answer += 1
        size = len(q)
        while size > 0:
            x, y, k = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if board[nx][ny] == 1:
                        if k == 0 and not visited[k + 1][nx][ny]:
                            if nx == Ex - 1 and ny == Ey - 1:
                                return answer
                            q.append((nx, ny, 1))
                            visited[k + 1][nx][ny] = 1
                    else:
                        if not visited[k][nx][ny]:
                            if nx == Ex-1 and ny == Ey-1:
                                return answer
                            q.append((nx, ny, k))
                            visited[k][nx][ny] = 1
            size -= 1

    return -1

print(bfs(Hx-1, Hy-1))


