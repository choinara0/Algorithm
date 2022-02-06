from collections import deque

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def bfs(place, x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [[0] * 5 for i in range(5)]
    visited[x][y] = 1

    while q:
        x, y, dist = q.popleft()
        if 0 < dist < 3 and place[x][y] == 'P':
            return False
        if dist > 2:
            break
        for _ in range(4):
            nx, ny, ndist = x + dx[_], y + dy[_], dist + 1
            if 0<=nx<5 and 0<=ny<5:
                if place[nx][ny] != 'X' and not visited[nx][ny]:
                    q.append((nx, ny, ndist))
                    visited[nx][ny] = 1

    return True

def solution(places):
    answer = []

    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(place, i, j):
                        flag = 0
        answer.append(flag)
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
### [1, 0, 1, 1, 1]