import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

M, N = map(int, sys.stdin.readline().split())
matrix = []
visited = [[0]* M for i in range(N)]
q = deque()
answer = 0

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1

flag = True
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            flag = False
            break
if flag and q:
    print(0)
    exit()


def bfs(answer, matrix, visited, q):
    while(1):
        q2 = deque()
        while q:
            x, y = q.popleft()

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if (0 <= new_x < N and 0 <= new_y < M) and (visited[new_x][new_y] == 0 and matrix[new_x][new_y] == 0):
                    q2.append((new_x, new_y))
                    visited[new_x][new_y] = 1
                    matrix[new_x][new_y] = 1

        q = q2
        if not q:
            break
        answer += 1

    return answer

answer = bfs(answer, matrix, visited, q)

for i in range(N):
    if 0 in matrix[i]:
        print(-1)
        exit(0)
print(answer)








