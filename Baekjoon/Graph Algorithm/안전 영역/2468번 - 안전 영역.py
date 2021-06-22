import sys
sys.setrecursionlimit(10 ** 6)


def dfs(v1, v2, h):
    visited[v1][v2] = 1

    for _ in move:
        new_x, new_y = v1 + _[0], v2 + _[1]
        if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N:
            continue
        elif matrix[new_x][new_y] > h and visited[new_x][new_y] == 0:
            dfs(new_x, new_y, h)

    return


N = int(sys.stdin.readline())
matrix = [[j for j in map(int, sys.stdin.readline().split())] for i in range(N)]
max_matrix = max(max(matrix))
max_safe = 1
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(1, max_matrix):
    visited = [[0]*N for i in range(N)]
    cnt = 0

    for x in range(N):
        for y in range(N):
            if matrix[x][y] > i and visited[x][y] == 0:
                dfs(x, y, i)
                cnt += 1

    max_safe = max(cnt, max_safe)

print(max_safe)

'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''
