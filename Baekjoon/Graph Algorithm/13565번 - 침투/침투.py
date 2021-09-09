import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
check = 'NO'


def dfs(i, j, visited):
    global check
    if check == 'YES':
        return
    visited[i][j] = True

    for _ in move:
        new_i, new_j = i + _[0], j + _[1]
        if new_i < 0 or new_j < 0 or new_i >= N or new_j >= M:
            continue
        elif new_i == (N - 1) and matrix[new_i][new_j] == 0:
            check = 'YES'
            return
        elif (visited[new_i][new_j] == False) and (matrix[new_i][new_j] == 0) :
            dfs(new_i, new_j, visited)
    return

queue = deque()
for i in range(1):
    for j in range(M):
        if check=='YES':
            break
        visited = [[False] * M for i in range(N)]
        if matrix[i][j] == 0:

            dfs(i, j, visited)

print(check)

'''
8 8
11000111
01100000
00011001
11001000
10001001
10111100
01010000
00001011
'''