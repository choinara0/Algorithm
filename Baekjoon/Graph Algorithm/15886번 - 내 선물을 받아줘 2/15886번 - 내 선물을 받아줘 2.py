import sys

N = int(sys.stdin.readline())
board = list(map(str, sys.stdin.readline().strip()))
visited = [0] * N
gift_cnt = 0

def dfs(x):
    global gift_cnt
    if visited[x]:
        return
    visited[x] = 1
    if board[x] == 'E':
        dfs(x+1)
    else:
        dfs(x-1)

for i in range(N):
    if not visited[i] and board[i] == 'E':
        dfs(i)
        gift_cnt += 1

print(gift_cnt)