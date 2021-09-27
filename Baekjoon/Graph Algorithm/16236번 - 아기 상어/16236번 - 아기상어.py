import sys
from collections import deque
N = int(sys.stdin.readline())
sx, sy = 0, 0
matrix = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            sx, sy = i, j
            matrix[i][j] = 0
            break
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]
eat = 0
time = 0
shark_size = 2
eat_flag = False
answer = 0
q, visited = deque([(sx, sy)]), set([(sx, sy)])

while q:
    size = len(q)
    q = deque(sorted(q))
    for _ in range(size):
        x, y = q.popleft()

        if matrix[x][y] != 0 and matrix[x][y] < shark_size:
            matrix[x][y] = 9
            eat += 1

            if eat == shark_size:
                shark_size += 1
                eat = 0

            q, visited = deque(), set([(x, y)])
            eat_flag = True

            answer = time

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if (0<=nx<N) and (0<=ny<N) and (nx, ny) not in visited:
                if matrix[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited.add((nx, ny))

        if eat_flag:
            eat_flag = False
            break
    time += 1
    print(time, q)

print(answer)

