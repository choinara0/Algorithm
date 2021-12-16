import sys
from collections import deque

N = int(sys.stdin.readline())
board = []
shark_x, shark_y = 0, 0
fish_cnt = 0
fish_arr = []
dx , dy = [-1, 0, 0, 1], [0, -1, 1, 0]

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if 0 <= board[i][j] <= 6:
            fish_cnt += 1
            fish_arr.append((i, j))

        elif board[i][j] == 9:
            shark_x, shark_y = i, j
            board[i][j] = 0




