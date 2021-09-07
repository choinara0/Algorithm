import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
matrix = []
visited = [[0]* C for i in range(R)]
q = deque()
final_o_count = 0
final_v_count = 0
for i in range(R):
    matrix.append(sys.stdin.readline())

for a in range(R):
    for b in range(C):
        if matrix[a][b] != '#' and visited[a][b] == 0:
            q.append((a,b))
            o_cnt = 0
            v_cnt = 0
            visited[a][b] = 1
            while q:
                x, y = q.popleft()
                if matrix[x][y] == 'o' :
                    o_cnt += 1
                elif matrix[x][y] == 'v':
                    v_cnt += 1
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]

                    if (0 <= new_x < R and 0 <= new_y < C) and matrix[new_x][new_y] != '#' and visited[new_x][new_y] == 0:
                        q.append((new_x, new_y))
                        visited[new_x][new_y] = 1
            if o_cnt > v_cnt:
                final_o_count += o_cnt
            elif v_cnt >= o_cnt:
                final_v_count += v_cnt



print(final_o_count, final_v_count)




