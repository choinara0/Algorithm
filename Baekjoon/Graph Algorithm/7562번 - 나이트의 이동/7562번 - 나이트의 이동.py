import sys
from collections import deque
T = int(sys.stdin.readline())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]
def bfs(matrix, destination_x, destination_y, q):

    while q:
        x, y = q.popleft()
        if x == destination_x and y == destination_y:
            return

        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if (0<=new_x<len(matrix) and 0<=new_y<len(matrix)) and matrix[new_x][new_y] == 0:
                matrix[new_x][new_y] = matrix[x][y] + 1
                q.append((new_x, new_y))


for t in range(T):
    l = int(sys.stdin.readline())
    matrix = [[0]*l for i in range(l)]
    current_x, current_y = map(int, sys.stdin.readline().split())
    destination_x, destination_y = map(int, sys.stdin.readline().split())
    if current_x == destination_x and current_y == destination_y:
        print(0)
        continue
    q = deque()
    q.append((current_x, current_y))
    bfs(matrix, destination_x, destination_y, q)
    print(matrix[destination_x][destination_y])




