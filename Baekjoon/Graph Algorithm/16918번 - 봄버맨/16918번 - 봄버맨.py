import sys
from collections import deque

def find_bomb():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bomb_list.append((i, j))
    return

def plant_bomb():
    for i in range(R):
        for j in range(C):
            if board[i][j] != 'O':
                board[i][j] = 'O'
    return

def detonate_bomb():
    while bomb_list:
        x, y = bomb_list.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<R and 0<=ny<C:
                if board[nx][ny] == 'O':
                    board[nx][ny] = '.'
    return

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
R, C, N = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for i in range(R)] #1단계
N -= 1 # 2단계

while N > 0:
    bomb_list = deque()
    find_bomb()
    plant_bomb()
    N -= 1
    if N == 0:
        break
    detonate_bomb()
    N -= 1

for i in range(R):
    print(''.join(map(str, board[i])))