import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [0] * 101
visited = [0] * 101
ladder = dict()
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a] = b
snake = dict()
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    snake[a] = b

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        x = q.popleft()
        for i in range(1, 7):
            nx = x + i
            if 0<=nx<=100 and not visited[nx]:
                if nx in ladder.keys():
                    nx = ladder[nx]
                if nx in snake.keys():
                    nx = snake[nx]
                if not visited[nx]:
                    q.append(nx)
                    visited[nx] = 1
                    board[nx] = board[x] + 1

bfs()
print(board[100])