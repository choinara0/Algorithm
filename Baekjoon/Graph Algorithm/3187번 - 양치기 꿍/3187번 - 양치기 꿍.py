import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for i in range(R)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
visited = [[0]*C for i in range(R)]
ans_vcnt, ans_kcnt = 0, 0

def bfs(x, y, z):
    global ans_kcnt, ans_vcnt
    q = deque()
    q.append((x, y))
    if z == 'v':
        v_cnt, k_cnt = 1, 0
    else:
        v_cnt, k_cnt = 0, 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and board[nx][ny] == '.':
                visited[nx][ny] = 1
                q.append((nx, ny))

            elif 0<=nx<R and 0<=ny<C and not visited[nx][ny] and board[nx][ny] == 'v':
                v_cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))

            elif 0<=nx<R and 0<=ny<C and not visited[nx][ny] and board[nx][ny] == 'k':
                k_cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))

    if v_cnt < k_cnt:
        ans_kcnt += k_cnt
    else:
        ans_vcnt += v_cnt

for i in range(R):
    for j in range(C):
        if not visited[i][j] and (board[i][j] == 'v' or board[i][j] == 'k'):
            visited[i][j] = 1
            bfs(i, j, board[i][j])

print(ans_kcnt, ans_vcnt)