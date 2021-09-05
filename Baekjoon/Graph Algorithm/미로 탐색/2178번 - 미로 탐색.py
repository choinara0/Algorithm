import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
q = deque()
q.append([0,0])
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
matrix = []
for i in range(N):
    temp = list(sys.stdin.readline())
    temp.pop(len(temp)-1)
    matrix.append(temp)
matrix[0][0] = 1

while(q):
    x, y = q.popleft()

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if (0<=new_x<N and 0<=new_y<M) and matrix[new_x][new_y] == '1':
            q.append([new_x, new_y])
            matrix[new_x][new_y] = matrix[x][y] + 1

print(matrix[N-1][M-1])

