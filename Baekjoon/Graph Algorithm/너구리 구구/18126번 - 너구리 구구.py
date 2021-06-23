import sys

sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
visited = [0 for i in range(N + 1)]
matrix = [[] for i in range(N + 1)]


def dfs(v, l):
    global sum_length
    flag = False

    for i in matrix[v]:
        if visited[i[0]] == 0:
            flag = True

    if flag == False:
        if l > sum_length:
            sum_length = l
        return

    for i in matrix[v]:
        if visited[i[0]] == 0:
            visited[i[0]] = 1
            dfs(i[0], l + i[1])
            visited[i[0]] = 0
    return


for i in range(N - 1):
    A, B, C = map(int, sys.stdin.readline().split())
    matrix[A].append([B, C])
    matrix[B].append([A, C])

sum_length = 0
visited[1] = 1
dfs(1, 0)
print(sum_length)