from collections import deque

def bfs(x, y, n, m, map):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    ans = [[-1] * m for i in range(n)]
    ans[x][y] = 1
    visited = [[0] * m for i in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and map[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                ans[nx][ny] = ans[qx][qy] + 1

    return ans[n-1][m-1]

def solution(maps):
    map = maps
    m = len(map[0])
    n = len(map)
    answer = bfs(0, 0, n, m, map)
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) # 11
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]) # -1

