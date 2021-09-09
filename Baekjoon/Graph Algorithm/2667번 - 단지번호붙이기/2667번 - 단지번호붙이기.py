import sys
from collections import deque
N = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
matrix = []
for i in range(N):
    matrix.append(list(sys.stdin.readline()))

count_list = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1':
            count = 1
            q = deque()
            q.append((i, j))
            matrix[i][j] = 0

            while (q):
                x, y = q.popleft()

                for k in range(4):
                    new_x = x + dx[k]
                    new_y = y + dy[k]

                    if (0 <= new_x < N and 0 <= new_y <= N) and matrix[new_x][new_y] == '1':
                        q.append((new_x, new_y))
                        matrix[new_x][new_y] = 0
                        count += 1
            count_list.append(count)

print(len(count_list))
count_list.sort()
for i in range(len(count_list)):
    print(count_list[i])
