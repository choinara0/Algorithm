import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
matrix = []
q = deque()

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
    matrix.append(temp)


for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                q.append((i, j, k))

while(q):
    z, x, y= q.popleft()

    for i in range(6):
        new_x = x + dx[i]
        new_y = y + dy[i]
        new_z = z + dz[i]

        if (0<=new_x<N and 0<=new_y<M and 0<=new_z<H) and matrix[new_z][new_x][new_y] == 0:

            q.append((new_z,new_x, new_y))
            matrix[new_z][new_x][new_y] = matrix[z][x][y] + 1

day = -1
z = 1
for i in matrix:
    for j in i:
        for k in j:
            if k==0:
                z = 0
            day = max(day, k)
if z==0:
    print(-1)
elif day == 1:
    print(0)
else:
    print(day-1)


