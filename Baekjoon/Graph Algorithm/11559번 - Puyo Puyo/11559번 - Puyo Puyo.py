import sys
from collections import deque

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
graph = []
answer = 0

for i in range(12):
    graph.append(list(map(str, sys.stdin.readline().strip())))

def bfs(x, y, z):
    q = deque()
    q.append([x, y])
    visited = [[0] * 6 for _ in range(12)]
    visited[x][y] = 1
    delete = [[x, y]]
    count = 1
    flag = 0

    while q:
        px, py = q.popleft()

        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]

            if 0>nx or nx>=12 or 0>ny or ny>=6:
                continue
            if graph[nx][ny] == z and not visited[nx][ny]:
                q.append([nx, ny])
                delete.append([nx, ny])
                visited[nx][ny] = 1
                count += 1

    if count >= 4:
        flag = 1
        for a, b in delete:
            graph[a][b] = '.'

    return flag

def gravity():
    for y in range(6):
        queue = deque()
        for x in range(11, -1, -1):
            if graph[x][y] != '.':
                queue.append(graph[x][y])
        for x in range(11, -1, -1):
            if queue:
                graph[x][y] = queue.popleft()
            else:
                graph[x][y] = '.'
    return


while True:
    check = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                check += bfs(i, j, graph[i][j])

    if check == 0:
        print(answer)
        break
    else:
        answer += 1
    gravity()