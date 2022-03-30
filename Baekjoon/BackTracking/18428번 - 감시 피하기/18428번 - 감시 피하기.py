import sys
from itertools import combinations
from collections import deque

def bfs():
    q = deque(t_list)
    while q:
        temp_x, temp_y = q.popleft()
        for i in range(4):
            x, y = temp_x, temp_y
            while True:
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if arr[nx][ny] == 'O':
                        break
                    elif arr[nx][ny] == 'S':
                        return False
                    x, y = nx, ny
                else:
                    break
    return True

N = int(sys.stdin.readline())
arr = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
x_list = []
t_list = []
check = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            x_list.append([i, j])
        elif arr[i][j] == 'T':
            t_list.append([i, j])

for comb in combinations(x_list, 3):
    for x, y in comb:
        arr[x][y] = 'O'
    if bfs():
        check = True
        break
    for x, y in comb:
        arr[x][y] = 'X'

if check:
    print('YES')
else:
    print('NO')