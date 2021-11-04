import sys
from collections import deque
from copy import deepcopy

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
N, M = map(int, sys.stdin.readline().split())
iceMatrix = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
year = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0]*M for i in range(N)]
    visited[x][y] = 1

    while q:
        qx, qy = q.popleft()

        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0<=nx<N and 0<=nx<M and visited[nx][ny] == 0 and newIceMatrix[nx][ny] != 0:
                visited[nx][ny] = 1
                newIceMatrix[nx][ny] = 0
                q.append((nx, ny))

def checkMelt():
    for i in range(N):
        for j in range(M):
            if iceMatrix[i][j] != 0:
                return False
    return True

def checkZero(x, y):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<N and 0<=ny<M and iceMatrix[nx][ny] == 0:
            cnt += 1
    return cnt

while True:
    year += 1
    if checkMelt():
        print(0)
        break
    newIceMatrix = [[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if iceMatrix[i][j] != 0:
                zeroCnt = checkZero(i, j)
                value = iceMatrix[i][j] - zeroCnt
                newIceMatrix[i][j] = value if value >= 0 else 0
    iceMatrix = deepcopy(newIceMatrix)

    cnt = 0
    for i in range(N):
        for j in range(M):
           if newIceMatrix[i][j] != 0:
               bfs(i, j)
               cnt += 1
    if cnt>=2:
        print(year)
        break
