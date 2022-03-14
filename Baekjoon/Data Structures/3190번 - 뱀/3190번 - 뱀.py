import sys
from collections import deque

def bfs():
    direction = 1
    time = 1
    x, y = 0, 0
    q = deque([[y, x]])
    board[0][0] = 2

    while q:
        x, y = x + dx[direction], y + dy[direction]
        if 0<=x<N and 0<=y<N and board[y][x] != 2:
            if not board[y][x] == 1:
                temp_y, temp_x = q.popleft()
                board[temp_y][temp_x] = 0
            board[y][x] = 2
            q.append([y, x])
            if time in move.keys():
                if move[time] == "L":
                    direction = (direction-1) % 4
                elif move[time] == 'D':
                    direction = (direction+1) % 4
            time += 1
        else:
            return time


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
board = [[0]*N for i in range(N)]
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1
L = int(sys.stdin.readline())
move = {}
for _ in range(L):
    x, c = map(str, sys.stdin.readline().split())
    move[int(x)] = c
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

print(bfs())