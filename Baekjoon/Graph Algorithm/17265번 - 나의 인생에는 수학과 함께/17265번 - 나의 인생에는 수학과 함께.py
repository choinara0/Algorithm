import sys
from collections import deque

N = int(sys.stdin.readline())
board = [list(map(str, sys.stdin.readline().split())) for i in range(N)]
dx, dy = [1, 0], [0, 1]
max_answer = float('-Inf')
min_answer = float('Inf')

def dfs(x, y, now, before):
    global max_answer, min_answer

    if x == N-1 and y == N-1:
        max_answer = max(max_answer, int(now))
        min_answer = min(min_answer, int(now))

    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny].isdigit():
                dfs(nx, ny, str(eval(now + before + board[nx][ny])), '')
            else:
                dfs(nx, ny, now, board[nx][ny])

    return

dfs(0, 0, board[0][0], '')
print(max_answer, min_answer)