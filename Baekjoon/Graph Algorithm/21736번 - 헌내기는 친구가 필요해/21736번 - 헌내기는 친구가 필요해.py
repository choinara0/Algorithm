import sys
sys.setrecursionlimit(10**6)

def dfs(r, c):
    visited[r][c] = 1
    if matrix[r][c] == 'P':
        global meet
        meet += 1
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<m and visited[nx][ny]==0:
            if matrix[nx][ny] != 'X':
                dfs(nx, ny)
    return

n, m = map(int, sys.stdin.readline().split())
visited = [[0]*m for i in range(n)]
matrix = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
meet = 0
for i in range(n):
    row = list(input())
    for j in range(len(row)):
        if "I" == row[j]:
            start_node_r = i
            start_node_c = j
    matrix.append(row)
dfs(start_node_r, start_node_c)

if meet==0:
    print("TT")
else:
    print(meet)





