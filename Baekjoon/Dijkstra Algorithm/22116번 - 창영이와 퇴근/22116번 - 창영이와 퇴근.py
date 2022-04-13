import sys
from collections import deque

def bfs(flag):
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and abs(arr[nx][ny] - arr[x][y]) <= flag:
                if nx == N-1 and ny == N-1:
                    return True
                q.append((nx, ny))
                visited[nx][ny] = 1

    return False

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
start = 0
end = max(map(max, arr)) - min(map(min, arr))
answer = 0

while start<=end:
    mid = (start+end) // 2
    if bfs(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)