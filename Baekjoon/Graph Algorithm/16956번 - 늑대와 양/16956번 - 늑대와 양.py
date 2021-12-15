import sys

R, C = map(int ,sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for i in range(R)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
check = False

for x in range(R):
    for y in range(C):
        if board[x][y] == 'W':
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<R and 0<=ny<C and board[nx][ny] == 'S':
                    check = True
                    break
        elif board[x][y] == 'S':
            continue
        elif board[x][y] == '.':
            board[x][y] = 'D'

if check:
    print(0)
else:
    print(1)
    for i in board:
        print(''.join(i))