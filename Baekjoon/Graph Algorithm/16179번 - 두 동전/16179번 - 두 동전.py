import sys
from collections import deque
N, M = map(int ,sys.stdin.readline().split())
matrix = []
for i in range(N):
    matrix.append(list(sys.stdin.readline())[0:-1])
q = deque()
temp = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'o':
            temp.append((i, j))
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
q.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))

def bfs():

    while q:
        x1, y1, x2, y2, cnt = q.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0<=nx1<N and 0<=nx2<N and 0<=ny1<M and 0<=ny2<M:
                if matrix[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if matrix[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                q.append((nx1, ny1, nx2, ny2, cnt+1))
            elif 0<=nx1<N and 0<=ny1<M:
                return cnt + 1
            elif 0<=nx2<N and 0<=ny2<M:
                return cnt + 1
            else:
                continue

    return -1

print(bfs())