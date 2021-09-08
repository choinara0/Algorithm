import sys
import copy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
matrix = []
virus_q = deque()
ans = 0
for i in range(N):
    matrix.append(list(map(int, (sys.stdin.readline().split()))))


def bfs():
    global ans
    w = copy.deepcopy(matrix)
    for i in range(N):
        for j in range(M):
            if w[i][j] == 2:
                virus_q.append((i, j))
    while(virus_q):
        x, y = virus_q.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if (0<=new_x<N and 0<=new_y<M) and w[new_x][new_y] == 0:
                w[new_x][new_y] = 2
                virus_q.append((new_x, new_y))
    cnt = 0
    for i in w:
        cnt += i.count(0)

    ans = max(cnt, ans)



def selectWall(count):
    if count == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    selectWall(count + 1)
                    matrix[i][j] = 0

# def selectWall(start, count):
#     if start == 3:
#         bfs()
#         return
#     else:
#         for i in range(start, N*M):
#             x = i // M
#             y = i % M
#             if matrix[x][y] == 0:
#                 matrix[x][y] = 1
#                 selectWall(start+1, count -1)
#                 matrix[x][y] = 0
selectWall(0)
print(ans)