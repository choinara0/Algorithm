import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split()) # N = 세로, M = 가로
visited = [[0]*M for i in range(N)]

cnt = 0
move = [(1,0), (-1,0), (0,1), (0,-1)]
matrix = []


def dfs(x, y):
    visited[x][y] = 1
    for _ in move:
        new_x, new_y = x + _[0], y+_[1]
        if new_x < 0 or new_y < 0 or new_x >= N or new_y >= M:
            continue
        elif visited[new_x][new_y] == 0 and matrix[new_x][new_y] >= T:
            dfs(new_x, new_y)
    return


for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    t = []
    for j in range(M):
        t.append(int(sum(temp[3*j:3*(j+1)])/3))
    matrix.append(t)

T = int(sys.stdin.readline())

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and matrix[i][j] >= T:
            dfs(i, j)
            cnt += 1

print(cnt)





